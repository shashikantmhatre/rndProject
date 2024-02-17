from antlr.generated.ExprParser import ExprParser
from language.Executor import Executor
from language.context.ContextManager import ContextManager
from language.context.Data import Data
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class WithPredicateResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.WithPredicateContext, contextmanager):
        nodeName = ctx.ID().getText()
        variable = contextmanager.getmemory().get(nodeName)

        if variable is not None:
            return self._filter_value(variable, ctx, contextmanager)

        current_context = contextmanager.getmemory().get("__current")
        # print(f'in with predicates with current_context : {current_context } ')
        if current_context is not None:
            if current_context.gettype() == DataType.LIST:
                ret_value = []
                for i in range(len(current_context.getvalue())):
                    # print(f'get {nodeName} from list in current context')
                    lst_item = current_context.getvalue()[i].get(nodeName)

                    if lst_item is None:
                        parent_node = current_context.getalias()
                        if self.process_child_algo(parent_node, nodeName, contextmanager):
                            lst_item = current_context.getvalue()[i].get(nodeName)

                    if lst_item is not None:
                        if isinstance(lst_item, list):
                            for item in lst_item:
                                ret_value.append(item)
                        else:
                            ret_value.append(lst_item)

                current_node = Data(ret_value, nodeName)
            else:
                # print(f'get {nodeName} in current context')
                lst_item = current_context.getvalue().get(nodeName)
                if lst_item is None:
                    parent_node = current_context.getalias()
                    if self.process_child_algo(parent_node, nodeName, contextmanager):
                        lst_item = current_context.getvalue().get(nodeName)
                current_node = Data(lst_item, nodeName)

            return self._filter_value(current_node, ctx, contextmanager)

        raise RuntimeError(f'No Such Element {nodeName} at {current_context}')

    def _filter_value(self, val, ctx:ExprParser.WithPredicateContext, contextmanager):
        ret_value = None
        parent_context = contextmanager.getmemory().get("__current")
        if ctx.booleanExp() is not None:
            # print(f'you have predicate {ctx.booleanExp().getText()}')
            if val.gettype() == DataType.LIST:
                ret_value = Data([], val.getalias())
                for i in range(len(val.getvalue())):
                    contextmanager.getmemory().add("__current", Data(val.getvalue()[i]))
                    if ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(),
                                                                                           contextmanager):
                        ret_value.getvalue().append(val.getvalue()[i])
                # return ret_value
            else:
                if ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(),
                                                                                       contextmanager):
                    ret_value = val
        else:
            ret_value = val
        contextmanager.getmemory().add("__current", parent_context)
        return ret_value


    def process_child_algo(self, parent_node_name:str, child_node_name:str, parent_contextmanager):
        algo = parent_contextmanager.getmemory().get("__algo")
        # print(f'Check if this node {child_node_name} is available in algo under {parent_node_name}')
        if algo is not None and algo[parent_node_name] is not None and algo[parent_node_name][child_node_name] is not None:
            child_contextmanager = ContextManager()
            child_contextmanager.getmemory().add("__current", parent_contextmanager.getmemory().get("__current"))
            child_contextmanager.getmemory().add("__algo", parent_contextmanager.getmemory().get("__algo"))
            child_contextmanager.getmemory().add("__root", parent_contextmanager.getmemory().get("__root"))
            Executor(child_contextmanager, algo[parent_node_name][child_node_name]).process()
            return True
        return False

    def getname(self):
        return ExprParser.WithPredicateContext.__name__
