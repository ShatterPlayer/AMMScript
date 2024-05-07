from antlr4 import *
import sys
from antlr.AMMScriptLexer import AMMScriptLexer
from antlr.AMMScriptParser import AMMScriptParser
from antlr4.error.ErrorListener import ErrorListener
from AMMScriptParserVisitor import AMMScriptParserVisitor

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def defaultError(self, line, column, msg):
        raise Exception("Błąd w linii " + str(line) + " w kolumnie " + str(column))

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.defaultError(line, column, msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        self.defaultError(startIndex, stopIndex, "Ambiguity")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        self.defaultError(startIndex, stopIndex, "Attempting full context")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        self.defaultError(startIndex, stopIndex, "Context sensitivity")

def interpret(code):
  
  lexer = AMMScriptLexer(InputStream(code))

  stream = CommonTokenStream(lexer)
  parser = AMMScriptParser(stream)
  
  parser.removeErrorListeners()
  parser.addErrorListener(MyErrorListener())

  visitor = AMMScriptParserVisitor()

  try:
    visitor.visit(parser.program())
  except Exception as e:
    print(e)
    results = visitor.getResults()
    results.append(str(e))
    return results

  return visitor.getResults()
