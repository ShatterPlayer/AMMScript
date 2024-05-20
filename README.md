# AMMScript
**Autorzy:**
 *Anna Jochymczyk*,
 *Monika Halek*,
 *Michał Karpierz*

## Założenia programu
AMM Script został stworzony z myślą o prostocie i intuicyjności, aby umożliwić łatwą naukę programowania nawet początkującym. Zestawiając najlepsze cechy dwóch popularnych języków - Pythona i C, AMM Script oferuje harmonijne połączenie elastyczności Pythona z efektywnością i strukturą C. AMM Script stawia sobie za cel zminimalizowanie frustracji początkujących programistów poprzez zapewnienie wsparcia w obsłudze błędów za pomocą jasnych komunikatów. Dodatkowo, automatyczne uzupełnianie nawiasów oraz aktywne monitorowanie składni poprzez odpowiednie podkreślenia mają na celu ułatwienie nauki poprzez zapewnienie wsparcia w trakcie pisania kodu.

**Języki implementacji:**
- Backend w AMM Script oparty jest głównie na języku Python, z dodatkowym wsparciem ANTLR i JavaScript w kontekście rozwoju.
- Do budowy interfejsu użytkownika wykorzystano CSS oraz TypeScript, który bazuje na JavaScript, we współpracy z frameworkiem Next JS.

**Sposób realizacji skanera/parsera**
- W projekcie skaner oraz parser zostały zaimplementowane przy użyciu generatora parserów ANTLR 4. Błędy w czasie wykonania obsługiwane są w trakcie przechodzenia po drzewie semantycznym [w visitor](https://github.com/ShatterPlayer/AMMScript/blob/master/AMMScriptParserVisitor.py).
  
## Opis tokenów
```
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

// Nawiasy:
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
// Stałe:
NUMBER: ('-')?[0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n])* '"';
// Typy logiczne
TRUE: 'true';
FALSE: 'false';
// Operatory logiczne
AND: '&&';
OR: '||';
NOT: '!';

// Komentarz:
COMMENT: '#' ~[\r\n]* -> skip;
// Inne znaki:
COMMA: ',';
SEMICOLON: ';';
COLON: ':';

// Identyfikator:
ID: [a-zA-Z_][a-zA-Z0-9_]*;
```


## Uruchomienie
### Instalacja ANTLR4
Szczegółowe informacje [tutaj](https://github.com/antlr/antlr4-tools/tree/master).

Na Windowsie można zainstalować przez `pip`:

```
  pip install antlr4-tools
```

> [!WARNING]
> Nie zawsze samo wywołanie powyższej komendy wystarczy.

### Generacja drzewa składniowego
```
antlr4-parse AMMScriptLexer.g4 AMMScriptParser.g4 program -gui
```

Potem można wpisać program do konsoli i zakończyć CTRL + Z.

Alternatywnie można uruchomić program z pliku:
```
antlr4-parse AMMScriptLexer.g4 AMMScriptParser.g4 program -gui program.amm
```

### Generacja kodu źródłowego
```
antlr4 -Dlanguage=Python3 .\AMMScriptLexer.g4 .\AMMScriptParser.g4 -o .\antlr\ -no-listener -visitor
```

### Uruchomienie aplikacji webowej

Należy pamiętać o uruchomieniu:
```
python interpretation_api.py ammscript.py
```

Kolejnym krokiem jest wpisanie w terminalu:
```
npm run dev
```
Pojawi się wtedy link http://localhost:3000, jeśli się go kliknie będzie widać poniższą stronę:
(podgląd)
![image](https://github.com/ShatterPlayer/AMMScript/assets/115782747/84b32b6c-4705-4efa-9940-20d6c96fad95)
![image](https://github.com/ShatterPlayer/AMMScript/assets/115782747/bd7341ac-c887-4d6c-ab61-9fc73e063542)

## Przykłady
Przykładowy program w języku AMMScript znajduje się w pliku `program.amm` (nie ma on sensu z logicznego punktu widzenia, służy tylko do prezentacji struktur dostępnych w języku).

Przykładowe drzewo składniowe dla wyrażenia `b = a^(2+2*2);` wygenerowane jedną z powyższych komend w sekcji [generacja drzewa składniowego](#generacja-drzewa-składniowego):

![aritmetic](data/aritmetic.png)

## Instrukcja obsługi

## Tokeny
## Gramatyka
## Pakiety zewnętrzne
## Przykłady użycia
