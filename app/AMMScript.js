import React, { useState } from "react";
import "./AMMScript.css";
import '../app/globals.css'
import axios from "axios";


export const AMMScript = () => {
  const [code, setCode] = useState(""); 
  const [consoleOutput, setConsoleOutput] = useState("");

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

  return (
    <div className="AMM-script">
      <div className="div">
        <div className="overlap">
          <a href="/" className="home-button">
            <div className="overlap-group">
              <div className="text-wrapper">Home</div>
            </div>
          </a>
          <div className="about-button">
            <div className="div-wrapper">
              <div className="text-wrapper-2">About</div>
            </div>
          </div>
          <div className="info-button">
            <div className="overlap-2">
              <div className="text-wrapper-3">Info</div>
            </div>
          </div>
        </div>
        <div className="overlap-3">
          <div className="background">
            <div className="overlap-4">
             <div className="rectangle"/>
              <div className="rectangle-2" />
              <textarea id="code-input" rows="10" cols="50" placeholder="AMM Script>" value={code} onChange={(e) => setCode(e.target.value)}></textarea>
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
                                                                          fontFamily: 'JetBrains Mono, monospace'}}>  
        </textarea>
      </div>
    </div>
  );
};
