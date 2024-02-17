from antlr.generated.ExprParser import ExprParser
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class NodeReferenceResolver(BaseResolver):
    def resolve(self, ctx: ExprParser.NodeReferenceContext, contextmanager):
        parent_context = contextmanager.getmemory().get("__current")
        current_context = ResolverRegistry().get(ctx.withPredicate().__class__.__name__).resolve(ctx.withPredicate(), contextmanager)
        if ctx.nodeReference() is not None and current_context is not None:
            # TODO check if current is not a dictionary then raise error
            # print(f'in NodeReferenceResolver with {ctx.getText()}')
            if not ( current_context.gettype() == DataType.LIST or current_context.gettype() == DataType.OBJECT ) :
                raise RuntimeError(f'Memory variable is { current_context.gettype() } and not a dictionary at line { ctx.getText()}')
            contextmanager.getmemory().add("__current", current_context)
            value = ResolverRegistry().get(ctx.nodeReference().__class__.__name__).resolve(ctx.nodeReference(), contextmanager)
            contextmanager.getmemory().add("__current", parent_context)
            return value
        return current_context

    def getname(self):
        return ExprParser.NodeReferenceContext.__name__
