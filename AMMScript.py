from antlr4 import *
import sys
from AMMScriptLexer import AMMScriptLexer
from AMMScriptParser import AMMScriptParser
from AMMScriptParserVisitor import AMMScriptParserVisitor

args = sys.argv
f = open(args[1], 'r')
lexer = AMMScriptLexer(InputStream(f.read()))

stream = CommonTokenStream(lexer)
parser = AMMScriptParser(stream)

visitor = AMMScriptParserVisitor()

visitor.visit(parser.program()) 

f.close()
