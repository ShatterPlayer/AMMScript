import ply.yacc as yacc
from lexer import tokens


def p_program(p):
    """
    program : statement_list
    """
    pass

def p_statement_list(p):
    """
    statement_list : statement
                   | statement_list statement
    """
    pass

def p_statement(p):
    """
    statement : variable_declaration SEMICOLON
              | variable_assignment SEMICOLON
              | PRINT expr SEMICOLON
              | IF LPAREN expr RPAREN LBRACE statement_list RBRACE
              | IF LPAREN expr RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
              | FOR LPAREN variable_declaration SEMICOLON expr SEMICOLON variable_assignment RPAREN LBRACE statement_list RBRACE
              | WHILE LPAREN expr RPAREN LBRACE statement_list RBRACE
    """
    pass

def p_variable_declaration(p):
    """
    variable_declaration : SET ID EQUAL expr
    """
    pass

def p_variable_assignment(p):
    """
    variable_assignment : ID EQUAL expr
    """
    pass

def p_expr(p):
    """
    expr : expr PLUS expr
         | expr MINUS expr
         | expr MULTIPLY expr
         | expr DIVIDE expr
         | expr MODULO expr
         | expr POWER expr
         | expr EQUAL_EQUAL expr
         | expr NOT_EQUAL expr
         | expr LESS expr
         | expr GREATER expr
         | expr LESS_EQUAL expr
         | expr GREATER_EQUAL expr
         | expr AND expr
         | expr OR expr
         | LPAREN expr RPAREN
         | NUMBER
         | ID
         | STRING
         | TRUE
         | FALSE
         | functionCall
         | unaryExpr
    """
    pass

def p_functionCall(p):
    """
    functionCall : ID LPAREN argument_list RPAREN
    """
    pass

def p_argument_list(p):
    """
    argument_list : expr
                  | argument_list COMMA expr
    """
    pass

def p_unaryExpr(p):
    """
    unaryExpr : PLUS expr
              | MINUS expr
              | NOT expr
    """
    pass

parser = yacc.yacc()
