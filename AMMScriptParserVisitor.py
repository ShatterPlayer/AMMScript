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

class ReturnException(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value


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
        from antlr.AMMScriptParser import AMMScriptParser
       
        for child in ctx.children:
            if isinstance(child, antlr4.tree.Tree.TerminalNode):
                if child.symbol.type == AMMScriptParser.RETURN:
                    expr_index = ctx.children.index(child) + 1
                    if expr_index < len(ctx.children):
                        expr_value = self.visit(ctx.children[expr_index])
                        raise ReturnException(expr_value)  
            else:
                self.visit(child)


    # Visit a parse tree produced by AMMScriptParser#statementInFunctionAndLoop.
    def visitStatementInFunctionAndLoop(self, ctx: AMMScriptParser.StatementInFunctionAndLoopContext):
        from antlr.AMMScriptParser import AMMScriptParser

        for child in ctx.children:
            if isinstance(child, antlr4.tree.Tree.TerminalNode):
                token_type = child.symbol.type
                if token_type == AMMScriptParser.RETURN:
                    expr_index = ctx.children.index(child) + 1
                    if expr_index < len(ctx.children):
                        expr_value = self.visit(ctx.children[expr_index])
                        raise ReturnException(expr_value)
                elif token_type == AMMScriptParser.BREAK:
                    raise BreakException()
                elif token_type == AMMScriptParser.CONTINUE:
                    raise ContinueException()
            else:
                try:
                    self.visit(child)
                except (BreakException, ContinueException, ReturnException) as e:
                    raise e


    # Visit a parse tree produced by AMMScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx: AMMScriptParser.VariableDeclarationContext):
        print("visitVariableDeclaration")
        variable_name = ctx.ID().getText()
        print("variable_name:", variable_name)
        if ctx.LBRACKET(0) != None:
            # Array
            arraySize = ctx.NUMBER().getText()

            if '.' in arraySize:
                raise Exception("Niepoprawny rozmiar tablicy")
            
            arraySize = int(arraySize)

            self.variables[variable_name] = []

            i = 0
            while i < arraySize:
                if ctx.expr(i) == None:
                    del self.variables[variable_name]
                    raise Exception("Niepoprawny rozmiar tablicy")
                self.variables[variable_name].append(self.visit(ctx.expr(i)))
                i += 1
            if ctx.expr(i) != None:
                raise Exception("Niepoprawny rozmiar tablicy")
        else:
            value = self.visit(ctx.expr(0))
            print("value:", value)
            self.variables[variable_name] = value

        print("variables:", self.variables)
        if ctx.LBRACKET(0) != None:
            # Array
            arraySize = ctx.NUMBER().getText()

            if '.' in arraySize:
                raise Exception("Niepoprawny rozmiar tablicy")
            
            arraySize = int(arraySize)

            self.variables[variable_name] = []

            i = 0
            while i < arraySize:
                if ctx.expr(i) == None:
                    del self.variables[variable_name]
                    raise Exception("Niepoprawny rozmiar tablicy")
                self.variables[variable_name].append(self.visit(ctx.expr(i)))
                i += 1
            if ctx.expr(i) != None:
                raise Exception("Niepoprawny rozmiar tablicy")
        else:
            value = self.visit(ctx.expr(0))
            print("value:", value)
            self.variables[variable_name] = value

        print("variables:", self.variables)
        return

    # Visit a parse tree produced by AMMScriptParser#variableAsignment.
    def visitVariableAsignment(self, ctx: AMMScriptParser.VariableAsignmentContext):
        print('visitVariableAsignment')
        if ctx.LBRACKET() != None:
            # Array
            variable_name = ctx.ID().getText()
            index = self.visit(ctx.expr(0))

            if variable_name not in self.variables:
                raise Exception(f"Tablica {variable_name} nie istnieje")
            
            if isinstance(index, int) == False:
                raise Exception("Niepoprawny indeks tablicy")
            
            index = int(index)

            if index >= len(self.variables[variable_name]):
                raise Exception(f"Indeks {index} poza zakresem tablicy {variable_name}")
            
            self.variables[variable_name][index] = self.visit(ctx.expr(1))
        else:
            variable_name = ctx.ID().getText()
            value = self.visit(ctx.expr(0))

            print("variable_name:", variable_name)
            print("value:", value)
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
                            while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                                self.visitStatementInFunction(ctx.children[j])
                                j += 1
                        except ReturnException:
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

    # Visit a parse tree produced by AMMScriptParser#ifInFunctionAndLoop.
    def visitIfInFunctionAndLoop(self, ctx: AMMScriptParser.IfInFunctionAndLoopContext):
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
                            while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                                self.visitStatementInFunctionAndLoop(ctx.children[j])
                                j += 1
                        except BreakException:
                            raise
                        except ContinueException:
                            raise
                        except ReturnException:
                            raise
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue

                    j = i + 2
                    try:
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visitStatementInFunctionAndLoop(ctx.children[j])
                            j += 1
                    except BreakException:
                        raise
                    except ContinueException:
                        raise
                    break
            i += 1

        return None

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
        print('visitLoopInFunction')
        if ctx.forLoopInFunction():
            return self.visitForLoopInFunction(ctx.forLoopInFunction())
        elif ctx.whileLoopInFunction():
            return self.visitWhileLoopInFunction(ctx.whileLoopInFunction())
        else:
            raise Exception("Nieznany typ pętli w kontekście LoopContext")

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
        print('visitForLoopInFunction')
        self.visit(ctx.variableDeclaration())
        while True:
            condition_result = self.visit(ctx.expr())
            if isinstance(condition_result, str):
                condition_result = float(condition_result) if condition_result.isdigit() else condition_result
            if not condition_result:
                break
            try:
                for statement in ctx.statementInFunctionAndLoop():
                    self.visit(statement)
                self.visit(ctx.variableAsignment())
            except ReturnException:
                raise
            except BreakException:
                break
            except ContinueException:
                continue

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
        print("visitWhileLoopInFunction")
        while True:

            condition = self.visit(ctx.expr())
            if not condition:
                break
            try:

                for statement in ctx.statementInFunctionAndLoop():
                    self.visit(statement)
            except ReturnException:
                raise
            except BreakException:
                break
            except ContinueException:
                continue
        return None

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
        print("visitSwitchInFunction")
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
                            try:
                                self.visit(ctx.children[j])
                                j += 1
                            except ReturnException:
                                raise
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
   
    def visitFunctionDeclaration(self, ctx: AMMScriptParser.FunctionDeclarationContext):
        from antlr.AMMScriptParser import AMMScriptParser
        print("visitFunctionDeclaration")
        func_name = ctx.ID(0).getText() 
        print(f"funkcja: {func_name}")
        
        parameters = {}
        params_ctx = ctx.children[ctx.children.index(ctx.LPAREN()) + 1:ctx.children.index(ctx.RPAREN())]
        i = 0
        while i < len(params_ctx):
            if isinstance(params_ctx[i], antlr4.tree.Tree.TerminalNode) and params_ctx[i].symbol.type == AMMScriptParser.ID:
                param_name = params_ctx[i].getText()
    
                if i + 1 < len(params_ctx) and params_ctx[i + 1].getText() == '=':
                    default_value = self.visit(params_ctx[i + 2]) 
                    parameters[param_name] = default_value
                    i += 3  
                else:
                    parameters[param_name] = None
                    i += 1
            else:
                i += 1  

        body = []
        body_ctx = ctx.children[ctx.children.index(ctx.LBRACE()) + 1:ctx.children.index(ctx.RBRACE())]
        for statement in body_ctx:
            if not isinstance(statement, antlr4.tree.Tree.TerminalNode):  
                body.append(statement)

        
        self.functions[func_name] = {
            'parameters': parameters,
            'body': body
        }
        print(f"Funkcja: {func_name} , parametry: {parameters}")


    
    
    def visitFunctionCall(self, ctx: AMMScriptParser.FunctionCallContext):
        from antlr.AMMScriptParser import AMMScriptParser

        print("visitFunctionCall")
        
        if not hasattr(ctx, 'already_executed'):
            setattr(ctx, 'already_executed', True)
        else:
            return

        func_name = ctx.ID().getText()  
        if func_name not in self.functions:
            raise Exception(f"Nie zdefiniowano funkcji '{func_name}'.")  
        
        func_info = self.functions[func_name]
        parameters = func_info['parameters']  
        body = func_info['body']  

        
        passed_arguments = [self.visit(arg) for arg in ctx.expr()]

        local_scope = {}
        arg_index = 0

        for param, def_val in parameters.items():
            if arg_index < len(passed_arguments):
                local_scope[param] = passed_arguments[arg_index]
            elif def_val is not None:
                local_scope[param] = def_val
            else:
                raise Exception(f"Brak domyślnego argumentu dla {param}")
            arg_index += 1  

        old_variables = self.variables.copy()
        self.variables.update(local_scope)

        return_value = None
        try:
            for statement in body:
                self.visit(statement)
        except ReturnException as e:
            return_value = e.value
        finally:
            self.variables = old_variables
        return return_value      



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
        from antlr.AMMScriptParser import AMMScriptParser
        print('visitExprNumber')
        if '.' in ctx.NUMBER().getText():
            return float(ctx.NUMBER().getText())
        else:
            return int(ctx.NUMBER().getText())


    # Visit a parse tree produced by AMMScriptParser#exprNumber.
    def visitExprVariable(self, ctx: AMMScriptParser.ExprNumberContext):
        print('visitExprNumber')
        return float(ctx.NUMBER().getText())

        
    def visitExprFunctionCall(self, ctx):
        
        print("visitExprFunctionCall")
        
        if hasattr(ctx, 'already_executed'):
            return getattr(ctx, 'result_return')
        else:
            setattr(ctx, 'already_executed', True)
            
            
            func_call_text = ctx.getText() 
            import re
            match = re.match(r"(\w+)\((.*)\)", func_call_text)
            if not match:
                raise Exception("zły format")

            func_name = match.group(1)
            argument_text = match.group(2)  

            if func_name not in self.functions:
                raise Exception(f"Nie zdefiniowano funkcji {func_name}")

            func_info = self.functions[func_name]
            parameters = func_info['parameters']
            body = func_info['body']

           
            passed_arguments = []
            if argument_text.strip():
                arguments = self.split_arguments(argument_text)
                for arg in arguments:
                    if arg.strip():
                        passed_arguments.append(eval(arg.strip()))

            if len(passed_arguments) != len(parameters):
                raise Exception(
                    f"Nieprawidłowa liczba parametrów, powinno być {len(parameters)}, a jest {len(passed_arguments)}")

            local_scope = self.assign_parameters(parameters, passed_arguments)

            old_variables = self.variables.copy()
            self.variables.update(local_scope)

            return_value = None
            try:
                for statement in body:
                    self.visit(statement)
            except ReturnException as e:
                return_value = e.value
            finally:
                self.variables = old_variables

            setattr(ctx, 'result_return', return_value)
            return return_value

          
    def split_arguments(self, argument_text):
        # bierze pod uwagę zagnieżdżone nawiasy
        args = []
        level = 0
        start = 0

        for i, char in enumerate(argument_text):
            if char == ',' and level == 0:
                args.append(argument_text[start:i].strip())
                start = i+1
            elif char == '(':
                level += 1
            elif char == ')':
                level -= 1

        if start < len(argument_text):
            args.append(argument_text[start:].strip())  

        return args


    def assign_parameters(self, parameters, passed_arguments):
        local_scope = {}
        for i, (param, default) in enumerate(parameters.items()):
            if i < len(passed_arguments):
                local_scope[param] = passed_arguments[i]
            elif default is not None:
                local_scope[param] = default
            else:
                raise Exception(f"Nie zdefiniowano domyślnej wartości dla {param}'")
            
        for i in list(local_scope):
            print(f"{i} : {local_scope[i]}")
        print(f"local scope : {list(local_scope)}")
        return local_scope

    # Visit a parse tree produced by AMMScriptParser#arrayExpr.
    def visitArrayExpr(self, ctx:AMMScriptParser.ArrayExprContext):
        variableName = ctx.ID().getText()
        index = self.visit(ctx.expr())

        print(index)
        if isinstance(index, int) == False:
            raise Exception("Niepoprawny indeks tablicy")


        if variableName not in self.variables:
            raise Exception(f"Tablica {variableName} nie istnieje")
        
        print("variableName:", variableName)
        print("index:", index)

        print('variables:', self.variables)

        index = int(index)

        if index >= len(self.variables[variableName]):
            raise Exception(f"Indeks {index} poza zakresem tablicy {variableName}")
        
        return self.variables[variableName][index]



del AMMScriptParser