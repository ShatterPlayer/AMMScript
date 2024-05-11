# AMMScript

## Jak uruchomić
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
