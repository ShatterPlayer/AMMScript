from parser import *
from lexer import *

def interpret(code):
    parser.parse(code)

if __name__ == '__main__':
    while True:
        try:
            s = input('AMM Script > ')
        except EOFError:
            break
        if not s:
            continue
        interpret(s)