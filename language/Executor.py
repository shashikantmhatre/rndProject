
from antlr4 import CommonTokenStream, InputStream

from antlr.generated.ExprLexer import ExprLexer
from antlr.generated.ExprParser import ExprParser
from language.context.ContextManager import ContextManager
from language.resolvers.ResolverRegistry import ResolverRegistry


class Executor:
    def __init__(self, contextmanager:ContextManager, block:str):
        self.contextmanager = contextmanager
        self.block = block

    def process(self):
        lexer = ExprLexer(InputStream(self.block))
        tokens = CommonTokenStream(lexer)
        parser = ExprParser(tokens)
        tree = parser.prog()
        # print(tree.toStringTree(recog=parser))
        ret_value = ResolverRegistry().get(tree.__class__.__name__).resolve(tree, self.contextmanager)
        # print(ret_value)
        return ret_value

