from antlr.generated.ExprParser import ExprParser
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class AssignStateResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.AssignStatContext, contextmanager):
        is_memory_variable = True
        variable_name = ctx.assignNode().ID(0).getText()
        current_context = contextmanager.getmemory().get(variable_name)

        if current_context is None:
            is_memory_variable = False
            current_context = contextmanager.getmemory().get("__current")

        if current_context is not None:
            assign_value = ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(),
                                                                                               contextmanager)
            if len(ctx.assignNode().ID()) > 1:
                # TODO we need to check what is the return type and perform operation
                self.assign_value(current_context, ctx.assignNode().ID(1).getText(), assign_value)
            elif len(ctx.assignNode().ID()) == 1:
                if is_memory_variable:
                    contextmanager.getmemory().add(ctx.assignNode().ID(0).getText(),ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(), contextmanager))
                else:
                    self.assign_value(current_context, variable_name, assign_value)
        else:
            raise RuntimeError(f'Could not find local variable named : {variable_name}')
        return None

    def assign_value(self, current_context, variable_name, assign_value):
        if current_context.gettype() == DataType.OBJECT:
            if assign_value is not None:
                current_context.getvalue()[variable_name] = assign_value.getvalue()
            else:
                current_context.getvalue()[variable_name] = None
        elif current_context.gettype() == DataType.LIST:
            for i in range(len(current_context.getvalue())):
                if isinstance(current_context.getvalue()[i], dict):
                    current_context.getvalue()[i][variable_name] = assign_value.getvalue()

    def getname(self):
        return ExprParser.AssignStatContext.__name__
