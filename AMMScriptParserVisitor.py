# Generated from AMMScriptParser.g4 by ANTLR 4.13.1
import inspect

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
        self.functions = {}
        self.parser = parser
        self.global_scope = {}
        self.scopes = [self.global_scope]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()
    
    def current_scope(self):
        return self.scopes[-1]

    def find_scope(self, var_name):
        for scope in reversed(self.scopes):
            if var_name in scope:
                return scope
        return None
    
    def set_variable(self, name, value):
        scope = self.find_scope(name)
        if scope is None:
            scope = self.current_scope()
        scope[name] = value

    def get_variable(self, name):
        scope = self.find_scope(name)
        if scope is None or name not in scope:
            raise Exception(f"Nie znaleziono zmiennej {name}")
        return scope[name]

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
        if ctx.BREAK():
            raise BreakException()
        elif ctx.CONTINUE():
            raise ContinueException()
        else:
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

        if ctx.LBRACKET(0) is not None:
            # Array
            array_size = int(ctx.NUMBER().getText())
            if '.' in ctx.NUMBER().getText():
                raise Exception("Niepoprawny rozmiar tablicy")

            array_elements = []
            for i in range(array_size):
                if ctx.expr(i) is None:
                    raise Exception("Niepoprawny rozmiar tablicy")
                array_elements.append(self.visit(ctx.expr(i)))
            
            self.current_scope()[variable_name] = array_elements

            if ctx.expr(array_size) is not None:
                raise Exception("Niepoprawny rozmiar tablicy")

            
        else:
            value = self.visit(ctx.expr(0))
            print("value:", value)
            self.current_scope()[variable_name] = value

        return

    # Visit a parse tree produced by AMMScriptParser#variableAsignment.
    def visitVariableAsignment(self, ctx: AMMScriptParser.VariableAsignmentContext):
        print('visitVariableAsignment')
        
        variable_name = ctx.ID().getText()
        
        if ctx.LBRACKET() is not None:
            # Array
            
            index = self.visit(ctx.expr(0))


            if isinstance(index, int) == False:
                raise Exception("Niepoprawny indeks tablicy")
            
            scope = self.find_scope(variable_name)
            if scope is None or variable_name not in scope:
                raise Exception(f"Tablica {variable_name} nie istnieje")

            index = int(index)
            array = scope[variable_name]

            if index >= len(array):
                raise Exception(f"Indeks {index} poza zakresem tablicy {variable_name}")

            array[index] = self.visit(ctx.expr(1))
        else:
            
            value = self.visit(ctx.expr(0))
            print("variable_name:", variable_name)
            print("value:", value)

            scope = self.find_scope(variable_name)
            if scope:
                scope[variable_name] = value
            else:
                raise Exception(f"Zmienna {variable_name} nie istnieje")
   
        return

    # Visit a parse tree produced by AMMScriptParser#print.
    def visitPrint(self, ctx: AMMScriptParser.PrintContext):
        print('visitPrint')
        expr_value = self.visit(ctx.expr())
        print("value: ", expr_value)

        if expr_value is None:
            raise Exception(f"Próba wypisania niezadeklarowanej wartości.")

        self.results.append(expr_value)
        return expr_value

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
                        self.push_scope()
                        j = i + 3
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visit(ctx.children[j])
                            j += 1
                        self.pop_scope()
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue
                    self.push_scope()
                    j = i + 2
                    while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                        self.visit(ctx.children[j])
                        j += 1
                    self.pop_scope()
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
                        self.push_scope()
                        j = i + 3
                        try:
                            while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                                self.visitStatementInLoop(ctx.children[j])
                                j += 1
                        except BreakException:
                            raise
                        except ContinueException:
                            raise
                        self.pop_scope()
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue
                    self.push_scope()
                    j = i + 2
                    try:
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visitStatementInLoop(ctx.children[j])
                            j += 1
                    except BreakException:
                        raise
                    except ContinueException:
                        raise
                    self.pop_scope()
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
                        self.push_scope()
                        j = i + 3
                        try:
                            while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                                self.visitStatementInFunction(ctx.children[j])
                                j += 1
                        except ReturnException:
                            self.pop_scope()
                            raise
                        self.pop_scope()
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue
                    self.push_scope()
                    j = i + 2
                    try:
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visitStatementInFunction(ctx.children[j])
                            j += 1
                    except ReturnException:
                        self.pop_scope()
                        raise
                    self.pop_scope()
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
                        self.push_scope()
                        j = i + 3
                        try:
                            while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                                self.visitStatementInFunctionAndLoop(ctx.children[j])
                                j += 1
                        except BreakException:
                            self.pop_scope()
                            raise
                        except ContinueException:
                            self.pop_scope()
                            raise
                        except ReturnException:
                            self.pop_scope()
                            raise
                        self.pop_scope()
                        break
                elif token_type == self.parser.ELSE:
                    if executed:
                        i += 1
                        continue
                    self.push_scope()
                    j = i + 2
                    try:
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visitStatementInFunctionAndLoop(ctx.children[j])
                            j += 1
                    except BreakException:
                        self.pop_scope()
                        raise
                    except ContinueException:
                        self.pop_scope()
                        raise
                    except ReturnException:
                        self.pop_scope()
                        raise
                    self.pop_scope()
                    break
            i += 1
        return None

    # Visit a parse tree produced by AMMScriptParser#loop.
    def visitLoop(self, ctx: AMMScriptParser.LoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#loopInFunction.
    def visitLoopInFunction(self, ctx: AMMScriptParser.LoopInFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by AMMScriptParser#forLoop.
    def visitForLoop(self, ctx: AMMScriptParser.ForLoopContext):
        print('visitForLoop')
        self.push_scope()
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
        self.pop_scope()

    # Visit a parse tree produced by AMMScriptParser#forLoopInFunction.
    def visitForLoopInFunction(self, ctx: AMMScriptParser.ForLoopInFunctionContext):
        print('visitForLoopInFunction')
        self.push_scope()
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
                self.pop_scope()
                raise
            except BreakException:
                break
            except ContinueException:
                continue
        self.pop_scope()


     # Visit a parse tree produced by AMMScriptParser#forOfLoop.
    def visitForOfLoop(self, ctx:AMMScriptParser.ForOfLoopContext):
        iterableVariable = ctx.ID(0).getText()

        if iterableVariable in self.current_scope():
            raise Exception(f"Zmienna {iterableVariable} już istnieje")

        arrayVariable = ctx.ID(1).getText()

        if arrayVariable not in self.current_scope():
            raise Exception(f"Tablica {arrayVariable} nie istnieje")

        array = self.current_scope().get(arrayVariable)

        if not isinstance(array, list):
            raise Exception(f"Zmienna {arrayVariable} nie jest tablicą")
        
        i = 0
        self.push_scope()
        while i < len(array):
            self.current_scope()[iterableVariable] = array[i]
            try:
                for statement in ctx.statementInLoop():
                    self.visit(statement)
            except BreakException:
                break
            except ContinueException:
                i += 1
                continue
            i += 1
        self.pop_scope()



    # Visit a parse tree produced by AMMScriptParser#forOfLoopInFunction.
    def visitForOfLoopInFunction(self, ctx:AMMScriptParser.ForOfLoopInFunctionContext):
        iterableVariable = ctx.ID(0).getText()

        if iterableVariable in self.current_scope():
            raise Exception(f"Zmienna {iterableVariable} już istnieje")

        arrayVariable = ctx.ID(1).getText()

        if arrayVariable not in self.current_scope():
            raise Exception(f"Tablica {arrayVariable} nie istnieje")

        array = self.current_scope().get(arrayVariable)

        if not isinstance(array, list):
            raise Exception(f"Zmienna {arrayVariable} nie jest tablicą")
        
        i = 0
        self.push_scope()
        while i < len(array):
            self.current_scope()[iterableVariable] =  array[i]
            try:
                for statement in ctx.statementInFunctionAndLoop():
                    self.visit(statement)
            except ReturnException:
                raise
            except BreakException:
                break
            except ContinueException:
                i += 1
                continue
            i += 1
        self.pop_scope()


    # Visit a parse tree produced by AMMScriptParser#whileLoop.
    def visitWhileLoop(self, ctx: AMMScriptParser.WhileLoopContext):
        print("visitWhileLoop")
        self.push_scope()
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

        self.pop_scope()
        return None

        # Visit a parse tree produced by AMMScriptParser#whileLoopInFunction.

    def visitWhileLoopInFunction(self, ctx: AMMScriptParser.WhileLoopInFunctionContext):
        print("visitWhileLoopInFunction")
        self.push_scope()
        while True:

            condition = self.visit(ctx.expr())
            if not condition:
                break
            try:

                for statement in ctx.statementInFunctionAndLoop():
                    self.visit(statement)
            except ReturnException:
                self.pop_scope()
                raise
            except BreakException:
                break
            except ContinueException:
                continue
        self.pop_scope()
        return None

    # Visit a parse tree produced by AMMScriptParser#switch.
    def visitSwitch(self, ctx: AMMScriptParser.SwitchContext):
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
                    case_expr = self.visit(ctx.children[i + 1])
                    if switch_value == case_expr or executed:
                        executed = True
                        self.push_scope()
                        j = i + 3
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            self.visit(ctx.children[j])
                            j += 1
                        self.pop_scope()
                        if j < len(ctx.children) and isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode) and \
                                ctx.children[j].getSymbol().type == self.parser.BREAK:
                            break
                        i = j
                        continue
                    i += 1
                elif token_type == self.parser.DEFAULT:
                    default_statements = ctx.children[i + 2:]
                    i += 1
                else:
                    i += 1
            else:
                i += 1

        if not executed and default_statements:
            self.push_scope()
            for stmt in default_statements:
                if isinstance(stmt, antlr4.tree.Tree.TerminalNode) and stmt.getText() == '}':
                    break
                self.visit(stmt)
            self.pop_scope()

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
                    case_expr = self.visit(ctx.children[i + 1])
                    if switch_value == case_expr or executed:
                        executed = True
                        self.push_scope()
                        j = i + 3
                        while j < len(ctx.children) and not isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode):
                            try:
                                self.visit(ctx.children[j])
                                j += 1
                            except ReturnException:
                                self.pop_scope()
                                raise
                        self.pop_scope()
                        if j < len(ctx.children) and isinstance(ctx.children[j], antlr4.tree.Tree.TerminalNode) and \
                                ctx.children[j].getSymbol().type == self.parser.BREAK:
                            break
                        i = j
                        continue
                    i += 1
                elif token_type == self.parser.DEFAULT:
                    default_statements = ctx.children[i + 2:]
                    i += 1
                else:
                    i += 1
            else:
                i += 1

        if not executed and default_statements:
            self.push_scope()
            try:
                for stmt in default_statements:
                    if isinstance(stmt, antlr4.tree.Tree.TerminalNode) and stmt.getText() == '}':
                        break
                    self.visit(stmt)
            except ReturnException:
                self.pop_scope()
                raise
            self.pop_scope()

        return None

    def visitFunctionDeclaration(self, ctx: AMMScriptParser.FunctionDeclarationContext):
        print("visitFunctionDeclaration")
        func_name = ctx.ID(0).getText()
        print(f"funkcja: {func_name}")
        from antlr.AMMScriptParser import AMMScriptParser
        
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

        self.current_scope()[func_name] = {
            'parameters': parameters,
            'body': body
        }

        print(f"Funkcja: {func_name}, parametry: {parameters}")

    def visitFunctionCall(self, ctx: AMMScriptParser.FunctionCallContext):
        print("visitFunctionCall")
        func_name = ctx.ID().getText()
        
        if func_name not in self.functions:
            raise Exception(f"Nie zdefiniowano funckji {func_name}.")

        func_info = self.functions[func_name]
        parameters = func_info['parameters']
        body = func_info['body']

        passed_arguments = [self.visit(arg) for arg in ctx.expr()]
        local_scope = {}

        for param, value in zip(parameters.keys(), passed_arguments):
            local_scope[param] = value

        for param in parameters.keys():
            if param not in local_scope:
                local_scope[param] = parameters[param]

        self.scopes.append(local_scope)
        previous_scope = self.current_scope()

        return_value = None
        try:
            for statement in body:
                self.visit(statement)
        except ReturnException as e:
            return_value = e.value
        finally:
            self.pop_scope()

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
            scope = self.find_scope(left)
            if scope and isinstance(scope[left], (int, float)):
                left = scope[left]
            else:
                raise Exception(f"Wyrażenie {left} nie ma wartości liczbowej")

        if isinstance(right, str):
            scope = self.find_scope(right)
            if scope and isinstance(scope[right], (int, float)):
                right = scope[right]
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

        if not isinstance(left, bool) or not isinstance(right, bool):
            raise ValueError("Operacje logiczne mogą być wykonywane tylko na typach bool")

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
            scope = self.find_scope(left)
            if scope and isinstance(scope[left], (int, float)):
                left = scope[left]
            else:
                raise Exception(f"Wyrażenie {left} nie ma wartości liczbowej")

        if isinstance(right, str):
            scope = self.find_scope(right)
            if scope and isinstance(scope[right], (int, float)):
                right = scope[right]
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

        if type(left) != type(right):
            raise TypeError("Nie można porównać wartości różnych typów")

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
        scope = self.find_scope(var_name)
        if scope is None:
            raise Exception(f"Próba wypisania niezadeklarowanej wartości.")
        return scope[var_name]

    # Visit a parse tree produced by AMMScriptParser#exprPower.
    def visitExprPower(self, ctx: AMMScriptParser.ExprPowerContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if type(left) == str or type(right) == str:
            raise Exception("Nie można wykonać operacji potęgowania na napisach")

        if left == 0 and right == 0:
            raise Exception("Nie można podnieść 0 do potęgi 0")

        if type(left) == bool or type(right) == bool:
            raise Exception("Nie można wykonać operacji potęgowania na typie bool")

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
        print('visitExprVariable')
        return float(ctx.NUMBER().getText())

    def count_default_parameters(self, parameters):
        count = 0
        for param_value in parameters.values():
            if isinstance(param_value, inspect.Parameter) and param_value.default != inspect.Parameter.empty:
                count += 1
        return count



    def visitFunctionCall(self, ctx: AMMScriptParser.FunctionCallContext):
        print("visitFunctionCall")
        func_name = ctx.ID().getText()

        if func_name not in self.functions:
            raise Exception(f"Nie zdefiniowano funkcji '{func_name}'.")

        func_info = self.functions[func_name]
        parameters = func_info['parameters']
        body = func_info['body']


        passed_arguments = [self.visit(arg) for arg in ctx.expr()]
        local_scope = {}
        for param, value in zip(parameters.keys(), passed_arguments):
            local_scope[param] = value

        for param in parameters.keys():
            if param not in local_scope:
                local_scope[param] = parameters[param]


        previous_scope = self.current_scope()
        self.scopes.append(local_scope)

        return_value = None
        try:
            for statement in body:
                self.visit(statement)
        except ReturnException as e:
            return_value = e.value
        finally:
            self.pop_scope()

        return return_value

    def split_arguments(self, argument_text):
        # bierze pod uwagę zagnieżdżone nawiasy
        args = []
        level = 0
        start = 0

        for i, char in enumerate(argument_text):
            if char == ',' and level == 0:
                args.append(argument_text[start:i].strip())
                start = i + 1
            elif char == '(':
                level += 1
            elif char == ')':
                level -= 1

        if start < len(argument_text):
            args.append(argument_text[start:].strip())

        return args

    def assign_parameters(self, parameters, passed_arguments):
        local_scope = {**self.current_scope()}
        param_names = list(parameters.keys())

        for i, arg in enumerate(passed_arguments):
            if i < len(param_names):
                param_name = param_names[i]
                local_scope.set(param_name, arg)
            else:
                raise Exception(f"Za dużo argumentów.")

       
        for param_name, default_value in parameters.items():
            if param_name not in local_scope.variables:
                if default_value is not None:
                    local_scope[param_name] = default_value
                else:
                    raise Exception(f"Nie podano wartości dla {param_name}")

        for param_name in local_scope:
            print(f"{param_name} : {local_scope[param_name]}")
        print(f"Local scope : {list(local_scope.keys())}")

        return local_scope

    # Visit a parse tree produced by AMMScriptParser#arrayExpr.
    def visitArrayExpr(self, ctx: AMMScriptParser.ArrayExprContext):
        variableName = ctx.ID().getText()
        index = self.visit(ctx.expr())

        print(index)
        if isinstance(index, int) == False:
            raise Exception("Niepoprawny indeks tablicy")

        scope = self.find_scope(variableName)
        if scope is None or variableName not in scope:
            raise Exception(f"Tablica {variableName} nie istnieje")

        print("variableName:", variableName)
        print("index:", index)


        index = int(index)

        if index >= len(scope[variableName]):
            raise Exception(f"Indeks {index} poza zakresem tablicy {variableName}")

        return scope[variableName][index]


del AMMScriptParser
