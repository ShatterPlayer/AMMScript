import ply.yacc as yacc
from lexer import *

variables = {}
def p_statement_expr(p):
    '''
    statement : expression SEMICOLON
    '''
    p[0] = p[1]

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression POWER expression
               | expression MODULO expression
               | expression EQUAL_EQUAL expression
               | expression NOT_EQUAL expression
               | expression LESS expression
               | expression GREATER expression
               | expression LESS_EQUAL expression
               | expression GREATER_EQUAL expression
               | expression EQUAL expression
               | expression PLUS_EQUAL expression
               | expression MINUS_EQUAL expression
               | expression MULTIPLY_EQUAL expression
               | expression DIVIDE_EQUAL expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '=':
        p[0] = p[3]
    elif p[2] == '+=':
        p[0] = p[1] + p[3]
    elif p[2] == '-=':
        p[0] = p[1] - p[3]
    elif p[2] == '*=':
        p[0] = p[1] * p[3]
    elif p[2] == '/=':
        p[0] = p[1] / p[3]

def p_statement_assign(p):
    '''
    statement : ID ASSIGN expression SEMICOLON
    '''
    variables[p[1]] = p[3]

def p_expression_variable(p):
    'expression : ID'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Undefined variable '{p[1]}'")
        p[0] = 0


def p_start(p):
    '''
    start : statement
          | expression
    '''
    print(p[1])
    p[0] = p[1]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_print(p):
    'expression : PRINT expression'
    print(p[2])
    p[0] = p[2]

def p_error(p):
    print("Błąd składni!")

parser = yacc.yacc()