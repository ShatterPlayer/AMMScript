from parser import *
from lexer import *

def interpret(code):
    try:
        return parser.parse(code)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    while True:
        try:
            s = input('AMM Script > ')
        except EOFError:
            break
        if not s:
            continue
        result = interpret(s)
