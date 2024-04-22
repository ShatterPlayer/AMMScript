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