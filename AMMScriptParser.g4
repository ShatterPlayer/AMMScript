parser grammar AMMScriptParser;
options {
	tokenVocab = AMMScriptLexer;
}

program: statement* EOF;

statement:
	variableDeclaration SEMICOLON
	| variableAsignment SEMICOLON
	| print SEMICOLON
	| functionCall SEMICOLON
	| expr SEMICOLON
	| if
	| loop
	| functionDeclaration
	| switch;

statementInLoop:
	variableDeclaration SEMICOLON
	| variableAsignment SEMICOLON
	| print SEMICOLON
	| functionCall SEMICOLON
	| expr SEMICOLON
	| ifInLoop
	| loop
	| BREAK
	| CONTINUE
	| switch;

statementInFunction:
	variableDeclaration SEMICOLON
	| variableAsignment SEMICOLON
	| print SEMICOLON
	| functionCall SEMICOLON
	| expr SEMICOLON
	| ifInFunction
	| loopInFunction
	| RETURN expr SEMICOLON
	| RETURN SEMICOLON
	| switchInFunction;

statementInFunctionAndLoop:
	variableDeclaration SEMICOLON
	| variableAsignment SEMICOLON
	| print SEMICOLON
	| functionCall SEMICOLON
	| expr SEMICOLON
	| ifInFunctionAndLoop
	| loopInFunction
	| BREAK
	| CONTINUE
	| RETURN expr SEMICOLON
	| RETURN SEMICOLON;

variableDeclaration: SET ID (EQUAL expr)?;
variableAsignment:
	ID (
		EQUAL
		| PLUS_EQUAL
		| MINUS_EQUAL
		| MULTIPLY_EQUAL
		| DIVIDE_EQUAL
	) expr;

print: PRINT expr;

if:
	IF expr LBRACE statement* RBRACE (
		ELSE IF expr LBRACE statement* RBRACE
	)* (ELSE LBRACE statement* RBRACE)?;

ifInLoop:
	IF expr LBRACE statementInLoop* RBRACE (
		ELSE IF expr LBRACE statementInLoop* RBRACE
	)* (ELSE LBRACE statementInLoop* RBRACE)?;

ifInFunction:
	IF expr LBRACE statementInFunction* RBRACE (
		ELSE IF expr LBRACE statementInFunction* RBRACE
	)* (ELSE LBRACE statementInFunction* RBRACE)?;

ifInFunctionAndLoop:
	IF expr LBRACE statementInFunctionAndLoop* RBRACE (
		ELSE IF expr LBRACE statementInFunctionAndLoop* RBRACE
	)* (ELSE LBRACE statementInFunctionAndLoop* RBRACE)?;

loop: forLoop | whileLoop;

loopInFunction: forLoopInFunction | whileLoopInFunction;

forLoop:
	FOR variableDeclaration SEMICOLON expr SEMICOLON variableAsignment LBRACE statementInLoop*
		RBRACE;

forLoopInFunction:
	FOR variableDeclaration SEMICOLON expr SEMICOLON variableAsignment LBRACE
		statementInFunctionAndLoop* RBRACE;

whileLoop: WHILE expr LBRACE statementInLoop* RBRACE;

whileLoopInFunction:
	WHILE expr LBRACE statementInFunctionAndLoop* RBRACE;

switch:
	SWITCH expr LBRACE (
		CASE expr COLON statement* (BREAK SEMICOLON)?
	)* (DEFAULT COLON statement* (BREAK SEMICOLON)?)? RBRACE;

switchInFunction:
	SWITCH expr LBRACE (
		CASE expr COLON statementInFunction* (BREAK SEMICOLON)?
	)* (DEFAULT COLON statementInFunction* (BREAK SEMICOLON)?)? RBRACE;

functionDeclaration:
	FUNCTION ID LPAREN (
		ID (EQUAL expr)? (COMMA ID (EQUAL expr)?)*
	)? RPAREN LBRACE statementInFunction* RBRACE;

functionCall: ID LPAREN (expr (COMMA expr)*)? RPAREN;

expr:
	LPAREN expr RPAREN
	| expr POWER expr
	| expr (MULTIPLY | DIVIDE | MODULO) expr
	| expr (PLUS | MINUS) expr
	| expr (
		EQUAL_EQUAL
		| NOT_EQUAL
		| LESS
		| GREATER
		| LESS_EQUAL
		| GREATER_EQUAL
	) expr
	| expr (AND | OR) expr
	| NUMBER
	| ID
	| STRING
	| TRUE
	| FALSE
	| functionCall
	| unaryExpr;

unaryExpr:
	ID PLUS_PLUS
	| ID MINUS_MINUS
	| PLUS_PLUS ID
	| MINUS_MINUS ID;