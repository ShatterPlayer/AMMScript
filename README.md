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
antlr4-parse AMMScriptLexer.g4 AMMScriptParser.g4 program -gui plik_z_programem.amm
```

## Przykłady
Przykładowy program w języku AMMScript znajduje się w pliku `program.amm` (nie ma on sensu z logicznego punktu widzenia, służy tylko do prezentacji struktur dostępnych w języku).

Przykładowe drzewo składniowe dla wyrażenia `b = a^(2+2*2);` wygenerowane jedną z powyższych komend w sekcji [generacja drzewa składniowego](#generacja-drzewa-składniowego):
![aritmetic](data/aritmetic.png)