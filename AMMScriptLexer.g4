lexer grammar AMMScriptLexer;

// Białe znaki:
WHITESPACE      : [ \t\r\n]+ -> skip;
// Słowa kluczowe:
SET             : 'set';
PRINT           : 'print';
IF              : 'if';
ELSE            : 'else';
FOR             : 'for';
WHILE           : 'while';
FUNCTION        : 'func';
RETURN          : 'return';
BREAK           : 'break';
CONTINUE        : 'continue';
// Operatory:
EQUAL           : '=';
NOT_EQUAL       : '!=';
SEMICOLON       : ';';
PLUS            : '+';
MINUS           : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
LESS            : '<';
GREATER         : '>';
LESS_EQUAL      : '<=';
GREATER_EQUAL   : '>=';
POWER : '^';
// Nawiasy:
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
// Identyfikator:
ID              : [a-zA-Z_][a-zA-Z0-9_]*;
// Stałe:
NUMBER          : [0-9]+;
STRING          : '"' (~["\r\n])* '"';
// Typy logiczne
TRUE            : 'true';
FALSE           : 'false';
// Operatory logiczne
AND             : '&&';
OR              : '||';
// Komentarz:
COMMENT         : '#' ~[\r\n]* -> skip;
// Inne znaki:
COMMA           : ',';
// Obsługa błędów:
ERROR           : . ;

