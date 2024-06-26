import React, { useState, useRef, useEffect } from 'react';
import "./AMMScript.css";
import '../app/globals.css'
import axios from "axios";
import Navbar from "../components/Navbar";
import Editor, { useMonaco } from "@monaco-editor/react";

export const AMMScript = () => {
  const [code, setCode] = useState(""); 
  const [consoleOutput, setConsoleOutput] = useState("");
  const [editorCode, setEditorCode] = useState('# Write your code here...');
  const editorRef = useRef(null);

  const monaco = useMonaco();

  const validateCode = (code) => {
    const markers = [];
  
    if (!code.trim()) {
      markers.push({
        startLineNumber: 1,
        startColumn: 1,
        endLineNumber: 1,
        endColumn: 1,
        message: "Kod nie może być pusty",
        severity: monaco.MarkerSeverity.Error
      });
    }
  
    if (!code.includes('print')) {
      markers.push({
        startLineNumber: 1,
        startColumn: 1,
        endLineNumber: 1,
        endColumn: 1,
        message: "Kod musi zawierać instrukcję 'print'",
        severity: monaco.MarkerSeverity.Warning
      });
    }
  
    const lines = code.split('\n');
    lines.forEach((line, index) => {
      const trimmedLine = line.trim();
      if (trimmedLine) {
        const startsWithKeyword = trimmedLine.startsWith("set") || trimmedLine.startsWith("print") || trimmedLine.startsWith("return") || trimmedLine.startsWith("break");
        const endsWithSemicolon = trimmedLine.endsWith(';');
        if (startsWithKeyword && !endsWithSemicolon) {
          markers.push({
            startLineNumber: index + 1,
            startColumn: 1,
            endLineNumber: index + 1,
            endColumn: line.length + 1,
            message: "Błąd składni: brakuje średnika ';' na końcu linii",
            severity: monaco.MarkerSeverity.Error
          });
        }
      }
    });
  
    return markers;
  };
  
  
  useEffect(() => {
    if (monaco) {
      monaco.languages.register({ id: 'ammLanguage' });
  
      monaco.languages.setMonarchTokensProvider('ammLanguage', {
        tokenizer: {
          root: [
            [/^#.*$/, 'comment'],
  
            [/\b(set|print|if|else|for|while|func|return|break|continue|switch|case|default)\b/, 'keyword'],
  
            [/==|!=|<=|>=|<|>/, 'operator'],
  
            [/=|\+=|-=|\*=|\/=/, 'operator'],
  
            [/\+|-|\*|\/|\^|%/, 'operator'],
  
            [/[(){}[\]]/, 'bracket'],
  
            [/(\-)?\d+(\.\d+)?/, 'number'],
  
            [/".*?"/, 'string'],
  
            [/\b(true|false)\b/, 'keyword'],
  
            [/&&|\|\||!/, 'operator'],
  
            [/,|;|:/, 'delimiter'],
  
            [/[a-zA-Z_][a-zA-Z0-9_]*/, 'identifier'],
  
            [/[ \t\r\n]+/, '']
          ]
        }
      });
  
      monaco.editor.defineTheme('ammTheme', {
        base: 'vs-dark',
        inherit: true,
        rules: [
          { token: 'comment', foreground: 'ffa500', fontStyle: 'italic' },
          { token: 'keyword', foreground: '569cd6' },
          { token: 'number', foreground: 'b5cea8' },
          { token: 'string', foreground: 'ce9178' },
          { token: 'operator', foreground: 'd4d4d4' },
          { token: 'bracket', foreground: 'd4d4d4' },
          { token: 'delimiter', foreground: 'd4d4d4' },
          { token: 'identifier', foreground: '9cdcfe' }
        ],
        colors: {
          'editor.background': '#000000', 
          'editorLineNumber.foreground': '#858585',
        },
      });
      monaco.editor.setTheme('ammTheme');

      monaco.languages.setLanguageConfiguration('ammLanguage', {
        surroundingPairs: [
          { open: '(', close: ')' },
          { open: '[', close: ']' },
          { open: '{', close: '}' },
          { open: '"', close: '"' }
        ],

        autoClosingPairs: [
          { open: '(', close: ')' },
          { open: '[', close: ']' },
          { open: '{', close: '}' },
          { open: '"', close: '"' }
        ],

        brackets: [
          ['(', ')'],
          ['[', ']'],
          ['{', '}'],
        ]
      })
    }
  }, [monaco]);

  const compile = () => {
    console.log("Running...");
    axios.post("http://localhost:5000/interpret", { code }) 
      .then(response => {
        console.log(response.data);
        setConsoleOutput(response.data.reduce((acc, curr) => acc + curr + "\n", ""));
      })
      .catch(error => {
        console.error("Błąd:", error);
        setConsoleOutput(`Błąd: ${error.message}`);
      });
  };
  

  const handleEditorDidMount = (editor) => {
    editorRef.current = editor;
  
    editor.onDidFocusEditorText(() => {
      if (editor.getValue() === '# Write your code here...') {
        setEditorCode('');
      }
    });
  
    editor.onDidBlurEditorText(() => {
      if (editor.getValue().trim() === '') {
        setEditorCode('# Write your code here...');
      }
    });
  
    if (monaco) {
      monaco.editor.setModelLanguage(editor.getModel(), 'ammLanguage');
      monaco.editor.setTheme('ammTheme');
      const markers = validateCode(editor.getValue());
      monaco.editor.setModelMarkers(editor.getModel(), 'owner', markers);
    }
  };
  

  const handleChange = (value) => {
    setEditorCode(value);
    setCode(value);
    if (monaco) {
      const markers = validateCode(value);
      monaco.editor.setModelMarkers(editorRef.current.getModel(), 'owner', markers);
    }
  };
  

  return (
    <div className="AMM-script">
      <div className="div">
        <Navbar/>
        <div className="overlap-3">
          <div className="background">
            <div className="overlap-4">
             <div className="rectangle"/>
              <div className="rectangle-2" />
              <div id="code-input">
              <Editor
                defaultLanguage="ammLanguage"
                value={editorCode}
                defaultValue="# Write your code here..."
                onChange={handleChange}
                onMount={handleEditorDidMount}
                theme="ammTheme"
                autoClo
              />
              </div>
              <img className="line" alt="Line" src="https://c.animaapp.com/a0hzXRiM/img/line-.svg" />
              <div className="text-wrapper-4">Source code:</div>
            </div>
          </div>
          <button className="compile-button" onClick={compile}>
              <div className="text-wrapper-5">Run</div>
          </button>
        </div>
        <div className="text-wrapper-6">© 2024 AMM Script</div>
        <div className="text-wrapper-7">AMM Script</div>
        <textarea id="console" placeholder="AMM Script Console>" value={consoleOutput} readOnly style={{ width: "1442px",
                                                                          height: "200px", 
                                                                          backgroundColor: "#b8b8b8", 
                                                                          border: "1px solid #ccc", 
                                                                          bottom: "0px", 
                                                                          overflowY: "auto", 
                                                                          cursor: "grab", 
                                                                          position: "fixed", 
                                                                          color: "white", 
                                                                          fontFamily: 'JetBrains Mono, monospace',
                                                                          paddingLeft: '20px',
                                                                          paddingTop: '20px'
                                                                          }}>  
        </textarea>
      </div>
    </div>
  );
};
