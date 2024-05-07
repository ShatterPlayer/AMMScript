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
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by AMMScriptParser#expr.
    def visitExpr(self, ctx:AMMScriptParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AMMScriptParser#unaryExpr.
    def visitUnaryExpr(self, ctx:AMMScriptParser.UnaryExprContext):
        return self.visitChildren(ctx)



del AMMScriptParser