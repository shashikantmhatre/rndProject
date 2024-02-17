# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stat.
    def visitStat(self, ctx:ExprParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#defStat.
    def visitDefStat(self, ctx:ExprParser.DefStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignStat.
    def visitAssignStat(self, ctx:ExprParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignNode.
    def visitAssignNode(self, ctx:ExprParser.AssignNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStat.
    def visitIfStat(self, ctx:ExprParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#elseStat.
    def visitElseStat(self, ctx:ExprParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#foreachStat.
    def visitForeachStat(self, ctx:ExprParser.ForeachStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forStat.
    def visitForStat(self, ctx:ExprParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addFunction.
    def visitAddFunction(self, ctx:ExprParser.AddFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#returnStat.
    def visitReturnStat(self, ctx:ExprParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ParenBoolean.
    def visitParenBoolean(self, ctx:ExprParser.ParenBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BooleanArithmetic.
    def visitBooleanArithmetic(self, ctx:ExprParser.BooleanArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#RelationalExp.
    def visitRelationalExp(self, ctx:ExprParser.RelationalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#LogicalExp.
    def visitLogicalExp(self, ctx:ExprParser.LogicalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ArithmeticNode.
    def visitArithmeticNode(self, ctx:ExprParser.ArithmeticNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ParenArithmetic.
    def visitParenArithmetic(self, ctx:ExprParser.ParenArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#UnaryArithmetic.
    def visitUnaryArithmetic(self, ctx:ExprParser.UnaryArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#node.
    def visitNode(self, ctx:ExprParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#objectNode.
    def visitObjectNode(self, ctx:ExprParser.ObjectNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listNode.
    def visitListNode(self, ctx:ExprParser.ListNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#getFunction.
    def visitGetFunction(self, ctx:ExprParser.GetFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#nodeReference.
    def visitNodeReference(self, ctx:ExprParser.NodeReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#withPredicate.
    def visitWithPredicate(self, ctx:ExprParser.WithPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#booleanValue.
    def visitBooleanValue(self, ctx:ExprParser.BooleanValueContext):
        return self.visitChildren(ctx)



del ExprParser