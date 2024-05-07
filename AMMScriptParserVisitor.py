# Generated from AMMScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from antlr.AMMScriptParser import AMMScriptParser
else:
    from antlr.AMMScriptParser import AMMScriptParser

# This class defines a complete generic visitor for a parse tree produced by AMMScriptParser.

class AMMScriptParserVisitor(ParseTreeVisitor):
    def __init__(self):
        self.results = []

    def getResults(self):
        return self.results

   # Visit a parse tree produced by AMMScriptParser#program.
    def visitProgram(self, ctx:AMMScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#statement.
    def visitStatement(self, ctx:AMMScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#statementInLoop.
    def visitStatementInLoop(self, ctx:AMMScriptParser.StatementInLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#statementInFunction.
    def visitStatementInFunction(self, ctx:AMMScriptParser.StatementInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#statementInFunctionAndLoop.
    def visitStatementInFunctionAndLoop(self, ctx:AMMScriptParser.StatementInFunctionAndLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:AMMScriptParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#variableAsignment.
    def visitVariableAsignment(self, ctx:AMMScriptParser.VariableAsignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#print.
    def visitPrint(self, ctx:AMMScriptParser.PrintContext):
        print('visitPrint')
        self.results.append(self.visit(ctx.expr()))
        return


    # Visit a parse tree produced by AMMScriptParser#if.
    def visitIf(self, ctx:AMMScriptParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#ifInLoop.
    def visitIfInLoop(self, ctx:AMMScriptParser.IfInLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#ifInFunction.
    def visitIfInFunction(self, ctx:AMMScriptParser.IfInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#ifInFunctionAndLoop.
    def visitIfInFunctionAndLoop(self, ctx:AMMScriptParser.IfInFunctionAndLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#loop.
    def visitLoop(self, ctx:AMMScriptParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#loopInFunction.
    def visitLoopInFunction(self, ctx:AMMScriptParser.LoopInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#forLoop.
    def visitForLoop(self, ctx:AMMScriptParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#forLoopInFunction.
    def visitForLoopInFunction(self, ctx:AMMScriptParser.ForLoopInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#whileLoop.
    def visitWhileLoop(self, ctx:AMMScriptParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#whileLoopInFunction.
    def visitWhileLoopInFunction(self, ctx:AMMScriptParser.WhileLoopInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#switch.
    def visitSwitch(self, ctx:AMMScriptParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#switchInFunction.
    def visitSwitchInFunction(self, ctx:AMMScriptParser.SwitchInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:AMMScriptParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#functionCall.
    def visitFunctionCall(self, ctx:AMMScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprTrue.
    def visitExprTrue(self, ctx:AMMScriptParser.ExprTrueContext):
        print('visitExprTrue')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#exprFalse.
    def visitExprFalse(self, ctx:AMMScriptParser.ExprFalseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#exprPlusMinus.
    def visitExprPlusMinus(self, ctx:AMMScriptParser.ExprPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprAndOr.
    def visitExprAndOr(self, ctx:AMMScriptParser.ExprAndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprMultDivMod.
    def visitExprMultDivMod(self, ctx:AMMScriptParser.ExprMultDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprComparison.
    def visitExprComparison(self, ctx:AMMScriptParser.ExprComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprString.
    def visitExprString(self, ctx:AMMScriptParser.ExprStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprId.
    def visitExprId(self, ctx:AMMScriptParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprUnary.
    def visitExprUnary(self, ctx:AMMScriptParser.ExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprPower.
    def visitExprPower(self, ctx:AMMScriptParser.ExprPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprParenthesis.
    def visitExprParenthesis(self, ctx:AMMScriptParser.ExprParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#exprNumber.
    def visitExprNumber(self, ctx:AMMScriptParser.ExprNumberContext):
        print('visitExprNumber')
        return ctx.NUMBER().getText()


    # Visit a parse tree produced by AMMScriptParser#exprFunctionCall.
    def visitExprFunctionCall(self, ctx:AMMScriptParser.ExprFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#unaryExpr.
    def visitUnaryExpr(self, ctx:AMMScriptParser.UnaryExprContext):
        return self.visitChildren(ctx)

del AMMScriptParser