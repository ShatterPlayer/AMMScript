parser grammar AMMScriptParser;
options { tokenVocab=AMMScriptLexer; }

program : statement* EOF;

statement : variableDeclaration SEMICOLON
          /*
               set a = 1;
               set b = "test";
               set c = true;
          */
          | variableAsignment SEMICOLON
          /*
               a = 1;
               b = "test";
               c = true;
          */
          | printStatement SEMICOLON
          /*
               print "test";
          */
          | errorStatement
          | ifStatement
          /*
               if a > b {

               } else if a > c {
                    
               } else {

               }
          */
          | loopStatement
          /*
               for set a=0; a < 10; a = a + 1 {

               }

               while a < 10 {

               }
          */
          | functionDeclaration
          /*
               func test(a, b="test") {
                    print a;
               }
          */
          | functionCall SEMICOLON
          /*
               test(1, 2);
               test(1=2, true);
          */
          | expr SEMICOLON
          | BREAK SEMICOLON
          | CONTINUE SEMICOLON
          | RETURN expr SEMICOLON
          | RETURN SEMICOLON;
          
variableDeclaration : SET ID (EQUAL expr)?;
variableAsignment : ID EQUAL expr;
printStatement : PRINT expr;
errorStatement : ERROR;

ifStatement : IF expr  
LBRACE statement* RBRACE 
(ELSE IF expr LBRACE statement* RBRACE)*
(ELSE LBRACE statement* RBRACE)?;

loopStatement : forLoop
              | whileLoop;

forLoop : FOR 
variableDeclaration SEMICOLON
expr SEMICOLON 
variableAsignment
LBRACE statement* RBRACE;

whileLoop : WHILE expr  
LBRACE statement* RBRACE;

functionDeclaration : FUNCTION ID LPAREN (ID (EQUAL expr)? (COMMA ID (EQUAL expr)?)*)? RPAREN LBRACE statement* RBRACE;

functionCall : ID LPAREN (expr (COMMA expr)*)? RPAREN;

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
     | FALSE
     | functionCall;