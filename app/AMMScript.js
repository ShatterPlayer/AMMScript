import React, { useState, useRef, useEffect } from 'react';
import "./AMMScript.css";
import '../app/globals.css'
import axios from "axios";
import Navbar from "../components/Navbar";
import Editor from "@monaco-editor/react";

export const AMMScript = () => {
  const [code, setCode] = useState(""); 
  const [consoleOutput, setConsoleOutput] = useState("");
  const [editorCode, setEditorCode] = useState('# Write your code here...');
  const editorRef = useRef(null);

  const compile = () => {
    console.log("Kompilacja w toku...");
    axios.post("http://localhost:5000/interpret", { code }) 
      .then(response => {
        const resultText = JSON.stringify(response.data);
        console.log(response.data);
        setConsoleOutput(resultText);
      })
      .catch(error => {
        console.error("Błąd:", error);
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
  };

  const handleChange = (value) => {
    setEditorCode(value);
    setCode(value); 
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
                  defaultLanguage="plaintext"
                  value={editorCode}
                  defaultValue="# Write your code here..."
                  onChange={handleChange}
                  onMount={handleEditorDidMount}
                  theme="vs-dark"
                />
              </div>
              <img className="line" alt="Line" src="https://c.animaapp.com/a0hzXRiM/img/line-.svg" />
              <div className="text-wrapper-4">Write your code below:</div>
            </div>
          </div>
          <button className="compile-button" onClick={compile}>
              <div className="text-wrapper-5">compile</div>
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
