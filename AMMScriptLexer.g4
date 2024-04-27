lexer grammar AMMScriptLexer;

// Białe znaki:
WHITESPACE: [ \t\r\n]+ -> skip;
// Słowa kluczowe:
SET: 'set';
PRINT: 'print';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
FUNCTION: 'func';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';

// Operatory porównania:
EQUAL_EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';

// Operatory przypisania:
EQUAL: '=';
PLUS_EQUAL: '+=';
MINUS_EQUAL: '-=';
MULTIPLY_EQUAL: '*=';
DIVIDE_EQUAL: '/=';

// Operatory arytmetyczne:
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
POWER: '^';
MODULO: '%';

// Operatory jednoargumentowe:
MINUS_MINUS: '--';
PLUS_PLUS: '++';

// Nawiasy:
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
// Identyfikator:
ID: [a-zA-Z_][a-zA-Z0-9_]*;
// Stałe:
NUMBER: [0-9]+;
STRING: '"' (~["\r\n])* '"';
// Typy logiczne
TRUE: 'true';
FALSE: 'false';
// Operatory logiczne
AND: '&&';
OR: '||';
// Komentarz:
COMMENT: '#' ~[\r\n]* -> skip;
// Inne znaki:
COMMA: ',';
SEMICOLON: ';';
COLON: ':';