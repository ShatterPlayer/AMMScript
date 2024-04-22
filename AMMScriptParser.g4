parser grammar AMMScriptParser;
options { tokenVocab=AMMScriptLexer; }

program : statement* EOF;

statement : assignment
          | printStatement
          | errorStatement
          | ifStatement
          | loopStatement
          | functionDeclaration
          | functionCall;
          
assignment : SET ID expr SEMICOLON;
printStatement : PRINT expr SEMICOLON;
errorStatement : ERROR;

ifStatement : IF expr  
LBRACE statement* RBRACE 
(ELSE LBRACE statement* RBRACE)?;

loopStatement : forLoop
              | whileLoop;

forLoop : FOR 
assignment 
expr SEMICOLON 
assignment
LBRACE statement* RBRACE;

whileLoop : WHILE expr  
LBRACE statement* RBRACE;

functionDeclaration : FUNCTION ID LPAREN (ID (EQUAL expr)? (COMMA ID (EQUAL expr)?)*)? RPAREN LBRACE statement* RBRACE;

functionCall : ID LPAREN (expr (COMMA expr)*)? RPAREN SEMICOLON;

expr : expr (PLUS | MINUS | MULTIPLY | DIVIDE) expr
     | expr (EQUAL | NOT_EQUAL 
            | LESS | GREATER 
            | LESS_EQUAL | GREATER_EQUAL) expr
     | expr (AND | OR) expr 
     | LPAREN expr RPAREN
     | NUMBER
     | ID
     | STRING
     | TRUE
     | FALSE;