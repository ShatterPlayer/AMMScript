from antlr4 import *
import sys
from antlr.AMMScriptLexer import AMMScriptLexer
from antlr.AMMScriptParser import AMMScriptParser
from AMMScriptParserVisitor import AMMScriptParserVisitor

def interpret(code):
  lexer = AMMScriptLexer(InputStream(code))

  stream = CommonTokenStream(lexer)
  parser = AMMScriptParser(stream)

  visitor = AMMScriptParserVisitor()

  visitor.visit(parser.program())

  return visitor.getResults()
