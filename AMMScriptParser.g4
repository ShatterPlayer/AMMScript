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
	| BREAK SEMICOLON
	| CONTINUE SEMICOLON
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
	| switchInFunction;

statementInFunctionAndLoop:
	variableDeclaration SEMICOLON
	| variableAsignment SEMICOLON
	| print SEMICOLON
	| functionCall SEMICOLON
	| expr SEMICOLON
	| ifInFunctionAndLoop
	| loopInFunction
	| BREAK SEMICOLON
	| CONTINUE SEMICOLON
	| RETURN expr SEMICOLON;

variableDeclaration: SET ID ((EQUAL expr) | (LBRACKET NUMBER RBRACKET EQUAL LBRACKET (expr (COMMA expr)*)? RBRACKET));
variableAsignment:
	ID (LBRACKET expr RBRACKET)? (
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

loop: forOfLoop | forLoop | whileLoop;

loopInFunction: forOfLoopInFunction | forLoopInFunction | whileLoopInFunction;

forLoop:
	FOR variableDeclaration SEMICOLON expr SEMICOLON variableAsignment LBRACE statementInLoop*
		RBRACE;

forLoopInFunction:
	FOR variableDeclaration SEMICOLON expr SEMICOLON variableAsignment LBRACE
		statementInFunctionAndLoop* RBRACE;

forOfLoop:
	FOR SET ID OF ID LBRACE statementInLoop* RBRACE;

forOfLoopInFunction:
	FOR SET ID OF ID LBRACE statementInFunctionAndLoop* RBRACE;

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

arrayExpr: ID LBRACKET expr RBRACKET;

expr:
	LPAREN expr RPAREN # exprParenthesis
	| expr POWER expr # exprPower
	| expr op=(MULTIPLY | DIVIDE | MODULO) expr # exprMultDivMod
	| expr op=(PLUS | MINUS) expr # exprPlusMinus
	| expr op=(
		EQUAL_EQUAL
		| NOT_EQUAL
		| LESS
		| GREATER
		| LESS_EQUAL
		| GREATER_EQUAL
	) expr # exprComparison
	| expr op=(AND | OR) expr # exprAndOr
	| NUMBER # exprNumber
	| STRING # exprString
	| TRUE # exprTrue
	| FALSE # exprFalse
	| functionCall # exprFunctionCall
	| arrayExpr # exprArray
	| ID # exprId;