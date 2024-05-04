import ply.lex as lex
from parser import *
from ply.lex import TOKEN

# Lista tokenów
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'POWER',
    'MODULO',
    'PRINT',
    'SEMICOLON',
    'EQUAL_EQUAL',
    'NOT_EQUAL',
    'LESS',
    'GREATER',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'EQUAL',
    'PLUS_EQUAL',
    'MINUS_EQUAL',
    'MULTIPLY_EQUAL',
    'DIVIDE_EQUAL',
    'ASSIGN',
    'ID'
)


# Reguły tokenów
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_MODULO = r'%'
t_PRINT = r'print'
t_SEMICOLON = r';'
t_EQUAL_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_EQUAL = r'='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_MULTIPLY_EQUAL = r'\*='
t_DIVIDE_EQUAL = r'/='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

reserved = {
    'print': 'PRINT'
}


# Ignorowane znaki (spacje)
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Obsługa błędów
def t_error(t):
    print(f"Nieznany symbol: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()