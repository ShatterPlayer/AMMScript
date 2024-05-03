import ply.lex as lex

tokens = [
    'SET', 'PRINT', 'IF', 'ELSE', 'FOR', 'WHILE', 'FUNCTION', 'RETURN', 'BREAK', 'CONTINUE',
    'SWITCH', 'CASE', 'DEFAULT', 'EQUAL_EQUAL', 'NOT_EQUAL', 'LESS', 'GREATER', 'LESS_EQUAL',
    'GREATER_EQUAL', 'EQUAL', 'PLUS_EQUAL', 'MINUS_EQUAL', 'MULTIPLY_EQUAL', 'DIVIDE_EQUAL',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'POWER', 'MODULO', 'MINUS_MINUS', 'PLUS_PLUS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'ID', 'NUMBER', 'STRING', 'TRUE', 'FALSE', 'AND', 'OR',
    'COMMA', 'SEMICOLON', 'COLON', 'COMMENT', 'NOT'
]

t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_MULTIPLY_EQUAL = r'\*='
t_DIVIDE_EQUAL = r'/='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_MODULO = r'%'
t_MINUS_MINUS = r'--'
t_PLUS_PLUS = r'\+\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'


def t_SET(t):
    r'set'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FUNCTION(t):
    r'func'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_EQUAL_EQUAL(t):
    r'=='
    return t

def t_NOT_EQUAL(t):
    r'!='
    return t

def t_LESS(t):
    r'<'
    return t

def t_GREATER(t):
    r'>'
    return t

def t_LESS_EQUAL(t):
    r'<='
    return t

def t_GREATER_EQUAL(t):
    r'>='
    return t

def t_EQUAL(t):
    r'='
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    return t

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()
