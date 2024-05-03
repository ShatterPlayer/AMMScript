from lexer import lexer
from parser import parser

def interpret(program):
    lexer.input(program)
    for tok in lexer:
        print(tok)

    parser.parse(program)

if __name__ == "__main__":
    while True:
        try:
            program = input("Enter program: ")
            interpret(program)
        except EOFError:
            break
