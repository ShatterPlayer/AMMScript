# Generated from AMMScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
from antlr.AMMScriptParser import AMMScriptParser
import re
import antlr4

# This class defines a complete generic visitor for a parse tree produced by AMMScriptParser.
class BreakException(Exception):
    pass


class ContinueException(Exception):
    pass


class AMMScriptParserVisitor(ParseTreeVisitor):
    def __init__(self, parser):
        self.results = []
        self.variables = {}
        self.functions = {}
        self.keywords = {}
        self.parser = parser

    def getResults(self):
        return self.results

    # Visit a parse tree produced by AMMScriptParser#program.
    def visitProgram(self, ctx: AMMScriptParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#statement.
    def visitStatement(self, ctx: AMMScriptParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#statementInLoop.
    def visitStatementInLoop(self, ctx: AMMScriptParser.StatementInLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#statementInFunction.
    def visitStatementInFunction(self, ctx: AMMScriptParser.StatementInFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#statementInFunctionAndLoop.
    def visitStatementInFunctionAndLoop(self, ctx: AMMScriptParser.StatementInFunctionAndLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx: AMMScriptParser.VariableDeclarationContext):
        print("visitVariableDeclaration")
        variable_name = ctx.ID().getText()
        print("variable_name:", variable_name)
        value = self.visit(ctx.expr(0))
        print("value:", value)
        self.variables[variable_name] = value
        return

    # Visit a parse tree produced by AMMScriptParser#variableAsignment.
    def visitVariableAsignment(self, ctx: AMMScriptParser.VariableAsignmentContext):
        print('visitVariableAsignment')
        variable_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[variable_name] = value
        return

    # Visit a parse tree produced by AMMScriptParser#print.
    def visitPrint(self, ctx: AMMScriptParser.PrintContext):
        print('visitPrint')
        expr_value = self.visit(ctx.expr())
        print("value: ", expr_value)

        if expr_value in self.variables:
            self.results.append(float(self.variables[expr_value]))
        else:
            self.results.append(expr_value)
        return

    def visitIf(self, ctx: AMMScriptParser.IfContext):
        print("visitIf")
        executed = False
        i = 0
        while i < len(ctx.children):
            child = ctx.children[i]
            if isinstance(child, antlr4.tree.Tree.TerminalNode):
                token_type = child.getSymbol().type
                if token_type == self.parser.IF or (
                        token_type == self.parser.ELSE and i + 1 < len(ctx.children) and ctx.children[i + 1].getSymbol().type == self.parser.IF):
                    if executed:
                        i += 1
                        continue
                    condition_expr = self.visit(ctx.children[i + 1])

                    if condition_expr:
                        executed = True

                        j = i + 3
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visit(ctx.children[j])
                            j += 1
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue

                    j = i + 2
                    while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                        self.visit(ctx.children[j])
                        j += 1
                    break
            i += 1

        return None

    # Visit a parse tree produced by AMMScriptParser#ifInLoop.
    def visitIfInLoop(self, ctx: AMMScriptParser.IfInLoopContext):
        print("visitIfInLoop")
        executed = False
        i = 0
        while i < len(ctx.children):
            child = ctx.children[i]
            if isinstance(child, antlr4.tree.Tree.TerminalNode):
                token_type = child.getSymbol().type
                if token_type == self.parser.IF or (
                        token_type == self.parser.ELSE and i + 1 < len(ctx.children) and ctx.children[i + 1].getSymbol().type == self.parser.IF):

                    if executed:
                        i += 1
                        continue

                    condition_expr = self.visit(ctx.children[i + 1])
                    if condition_expr:
                        executed = True

                        j = i + 3
                        try:
                            while j < len(ctx.children) and not isinstance(ctx.children[j],
                                                                           antlr4.tree.Tree.TerminalNode):
                                self.visitStatementInLoop(ctx.children[j])
                                j += 1
                        except BreakException:
                            raise
                        except ContinueException:
                            raise
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue

                    j = i + 2
                    try:
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visitStatementInLoop(ctx.children[j])
                            j += 1
                    except BreakException:
                        raise
                    except ContinueException:
                        raise
                    break
            i += 1

        return None

    # Visit a parse tree produced by AMMScriptParser#ifInFunction.
    def visitIfInFunction(self, ctx: AMMScriptParser.IfInFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#ifInFunctionAndLoop.
    def visitIfInFunctionAndLoop(self, ctx: AMMScriptParser.IfInFunctionAndLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#loop.
    def visitLoop(self, ctx: AMMScriptParser.LoopContext):
        print('visitLoop')
        if ctx.forLoop():
            return self.visitForLoop(ctx.forLoop())
        elif ctx.whileLoop():
            return self.visitWhileLoop(ctx.whileLoop())
        else:
            raise Exception("Nieznany typ pętli w kontekście LoopContext")

    # Visit a parse tree produced by AMMScriptParser#loopInFunction.
    def visitLoopInFunction(self, ctx: AMMScriptParser.LoopInFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#forLoop.
    def visitForLoop(self, ctx: AMMScriptParser.ForLoopContext):
        print('visitForLoop')
        self.visit(ctx.variableDeclaration())
        while True:
            condition_result = self.visit(ctx.expr())
            if isinstance(condition_result, str):
                condition_result = float(condition_result) if condition_result.isdigit() else condition_result
            if not condition_result:
                break
            try:
                for statement in ctx.statementInLoop():
                    self.visit(statement)
                self.visit(ctx.variableAsignment())
            except BreakException:
                break
            except ContinueException:
                continue

    # Visit a parse tree produced by AMMScriptParser#forLoopInFunction.
    def visitForLoopInFunction(self, ctx: AMMScriptParser.ForLoopInFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#whileLoop.
    def visitWhileLoop(self, ctx: AMMScriptParser.WhileLoopContext):
        print("visitWhileLoop")
        while True:

            condition = self.visit(ctx.expr())
            if not condition:
                break
            try:

                for statement in ctx.statementInLoop():
                    self.visit(statement)
            except BreakException:
                break
            except ContinueException:
                continue
        return None

        # Visit a parse tree produced by AMMScriptParser#whileLoopInFunction.

    def visitWhileLoopInFunction(self, ctx: AMMScriptParser.WhileLoopInFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#switch.
    def visitSwitch(self, ctx:AMMScriptParser.SwitchContext):
        print("visitSwitch")
        switch_value = self.visit(ctx.expr(0))

        executed = False
        default_statements = None

        i = 2  
        while i < len(ctx.children) - 1: 
            child = ctx.children[i]
            if isinstance(child, antlr4.tree.Tree.TerminalNode):
                token_type = child.getSymbol().type
                if token_type == self.parser.CASE:
                    case_expr = self.visit(ctx.children[i+1])
                    if switch_value == case_expr or executed:
                        executed = True  
                        j = i + 3 
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visit(ctx.children[j])
                            j += 1
                        if j < len(ctx.children) and isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode) and ctx.children[j].getSymbol().type == self.parser.BREAK:
                            break
                        i = j  
                        continue  
                    i += 1  
                elif token_type == self.parser.DEFAULT:
                    default_statements = ctx.children[i+2:]
                    i += 1  
                else:
                    i += 1  
            else:
                i += 1  

        if not executed and default_statements:
            for stmt in default_statements:
                if isinstance(stmt, antlr4.tree.Tree.TerminalNode) and stmt.getText() == '}':
                    break
                self.visit(stmt)

        return None


    # Visit a parse tree produced by AMMScriptParser#switchInFunction.
    def visitSwitchInFunction(self, ctx: AMMScriptParser.SwitchInFunctionContext):
        return self.visitChildren(ctx)

    def visitFunctionDeclaration(self, ctx: AMMScriptParser.FunctionDeclarationContext):
        from antlr.AMMScriptParser import AMMScriptParser
        print("visitFunctionDeclaration")

        function_name = ctx.ID(0).getText()
        print("function_name: ", function_name)

        parametersList = []

        for i in range(1, len(ctx.ID())):
            if ctx.ID(i):
                print("i", ctx.ID(i).getText())
                parametersList.append(ctx.ID(i).getText())

        print("parametersList:", parametersList)

        function_block = ctx.statementInFunction(0).getText()
        print("function_block: ", function_block)

        if function_name in self.functions:
            errorMsg = "Nazwa funkcji '{}' już zdefiniowana"
            return VisitorError(errorMsg.format(function_name))
        parametersSet = set(parametersList)
        if not (len(parametersSet) == len(parametersList)):
            errorMsg = "Parametry w funkcji '{}' mają już taką samą nazwę"
            return VisitorError(errorMsg.format(function_name))

        self.functions[function_name] = (parametersList, function_block)

        print(self.functions.items())


    # Visit a parse tree produced by AMMScriptParser#functionCall.
    def visitFunctionCall(self, ctx: AMMScriptParser.FunctionCallContext):
        from antlr.AMMScriptParser import AMMScriptParser
        from antlr.AMMScriptLexer import AMMScriptLexer
        print("visitFunctionCall")

        function_name = ctx.ID().getText()
        print("function_name:", function_name)

        values = []
        param_count = len(ctx.expr())
        print("param_count: ", param_count)

        for i in range(param_count):
            expr_ctx = ctx.expr(i)
            if isinstance(expr_ctx, AMMScriptParser.ExprIdContext):
                value = self.visitExprId(expr_ctx)
            else:
                value = self.visit(expr_ctx)

            values.append(value)

        print("values: ", values)
        print(self.functions.keys())
        print("self.functions.get(function_name): ", self.functions.get(function_name))

        parametersList, function_block = self.functions.get(function_name)

        if len(values) != param_count:
            errorMsg = "Nieodpowiednia liczba parametrów w funkcji '{}', oczekiwano {}, ale {} otrzymano"
            return VisitorError(errorMsg.format(function_name, param_count, len(values)))

        for i in range(param_count):
            self.variables[parametersList[i]] = float(values[i])

        print("variables: ", self.variables)

        if function_block.startswith("return"):
            function_block = function_block[len("return"):].strip()

        print("After modification:", function_block)

        input_stream = InputStream(function_block)
        lexer = AMMScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AMMScriptParser(stream)
        tree = parser.program()

        ret = self.visit(tree)

        return ret

    # Visit a parse tree produced by AMMScriptParser#exprTrue.
    def visitExprTrue(self, ctx: AMMScriptParser.ExprTrueContext):
        return True

    # Visit a parse tree produced by AMMScriptParser#exprFalse.
    def visitExprFalse(self, ctx: AMMScriptParser.ExprFalseContext):
        return False

    # Visit a parse tree produced by AMMScriptParser#exprPlusMinus.
    def visitExprPlusMinus(self, ctx: AMMScriptParser.ExprPlusMinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        from antlr.AMMScriptParser import AMMScriptParser

        if isinstance(left, str):
            if left in self.variables and isinstance(self.variables[left], (int, float)):
                left = self.variables[left]
            else:
                raise Exception(f"Wyrażenie {left} nie ma wartości liczbowej")

        if isinstance(right, str):
            if right in self.variables and isinstance(self.variables[right], (int, float)):
                right = self.variables[right]
            else:
                raise Exception(f"Wyrażenie {right} nie ma wartości liczbowej")

        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            if ctx.op.type == AMMScriptParser.PLUS:
                return left + right
            elif ctx.op.type == AMMScriptParser.MINUS:
                return left - right
        else:
            raise Exception("Nie można wykonać operacji matematycznych na napisach")

    # Visit a parse tree produced by AMMScriptParser#exprAndOr.
    def visitExprAndOr(self, ctx: AMMScriptParser.ExprAndOrContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # ! Nie wiem dlaczego tak trzeba ale bez tego nie działa
        from antlr.AMMScriptParser import AMMScriptParser

        if ctx.op.type == AMMScriptParser.AND:
            return left and right
        elif ctx.op.type == AMMScriptParser.OR:
            return left or right

    # Visit a parse tree produced by AMMScriptParser#exprMultDivMod.
    def visitExprMultDivMod(self, ctx: AMMScriptParser.ExprMultDivModContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # ! Nie wiem dlaczego tak trzeba ale bez tego nie działa
        from antlr.AMMScriptParser import AMMScriptParser

        if isinstance(left, str):
            if left in self.variables and isinstance(self.variables[left], (int, float)):
                left = self.variables[left]
            else:
                raise Exception(f"Wyrażenie {left} nie ma wartości liczbowej")

        if isinstance(right, str):
            if right in self.variables and isinstance(self.variables[right], (int, float)):
                right = self.variables[right]
            else:
                raise Exception(f"Wyrażenie {right} nie ma wartości liczbowej")

        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            if right == 0 and ctx.op.type == AMMScriptParser.DIVIDE:
                raise Exception("Nie można dzielić przez 0")

        if ctx.op.type == AMMScriptParser.MULTIPLY:
            return left * right
        elif ctx.op.type == AMMScriptParser.DIVIDE:
            return left / right
        elif ctx.op.type == AMMScriptParser.MODULO:
            return left % right

        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#exprComparison.
    def visitExprComparison(self, ctx: AMMScriptParser.ExprComparisonContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if isinstance(left, str):
            left = float(left) if left.isdigit() else left
        if isinstance(right, str):
            right = float(right) if right.isdigit() else right

        # ! Nie wiem dlaczego tak trzeba ale bez tego nie działa
        from antlr.AMMScriptParser import AMMScriptParser

        if ctx.op.type == AMMScriptParser.EQUAL_EQUAL:
            return left == right
        elif ctx.op.type == AMMScriptParser.NOT_EQUAL:
            return left != right
        elif ctx.op.type == AMMScriptParser.LESS:
            return left < right
        elif ctx.op.type == AMMScriptParser.LESS_EQUAL:
            return left <= right
        elif ctx.op.type == AMMScriptParser.GREATER:
            return left > right
        elif ctx.op.type == AMMScriptParser.GREATER_EQUAL:
            return left >= right

    # Visit a parse tree produced by AMMScriptParser#exprString.
    def visitExprString(self, ctx: AMMScriptParser.ExprStringContext):
        return ctx.STRING().getText()[1:-1]

    # Visit a parse tree produced by AMMScriptParser#exprId.
    def visitExprId(self, ctx: AMMScriptParser.ExprIdContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            return self.variables[var_name]


    # Visit a parse tree produced by AMMScriptParser#exprPower.
    def visitExprPower(self, ctx: AMMScriptParser.ExprPowerContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if type(left) == str or type(right) == str:
            raise Exception("Nie można wykonać operacji potęgowania na napisach")

        if left == 0 and right == 0:
            raise Exception("Nie można podnieść 0 do potęgi 0")

        return left ** right

    # Visit a parse tree produced by AMMScriptParser#exprParenthesis.
    def visitExprParenthesis(self, ctx: AMMScriptParser.ExprParenthesisContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by AMMScriptParser#exprArray.
    def visitExprArray(self, ctx: AMMScriptParser.ExprArrayContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#exprNumber.
    def visitExprNumber(self, ctx: AMMScriptParser.ExprNumberContext):
        print('visitExprNumber')
        return float(ctx.NUMBER().getText())

    # Visit a parse tree produced by AMMScriptParser#exprNumber.
    def visitExprVariable(self, ctx: AMMScriptParser.ExprNumberContext):
        print('visitExprNumber')
        return float(ctx.NUMBER().getText())

    # Visit a parse tree produced by AMMScriptParser#exprFunctionCall.
    def visitExprFunctionCall(self, ctx: AMMScriptParser.ExprFunctionCallContext):
        import re
        from antlr.AMMScriptParser import AMMScriptParser

        print("visitExprFunctionCall")
        print(ctx.functionCall().getText())
        function_name = ctx.functionCall().getText()
        function_name = (re.search(r'^.*?(?=\()', function_name)).group()

        if function_name in self.functions:
            function_block = self.functions[function_name][1]
            print("function_block: ", function_block)
            return self.visit(ctx.functionCall())
        else:
            raise Exception(f"Funkcja '{function_name}' nie jest zdefiniowana")

    # Visit a parse tree produced by AMMScriptParser#arrayExpr.
    def visitArrayExpr(self, ctx: AMMScriptParser.ArrayExprContext):
        return self.visitChildren(ctx)



del AMMScriptParser