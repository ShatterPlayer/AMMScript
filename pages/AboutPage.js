import React, { useState } from "react";
import "./AboutPage.css";
import '../app/globals.css'


export const AboutPage = () => {
  return (
    <div className="About-page">
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
              <div className="rectangle-2"/>
              <div className="code-input"/>
              <img className="line" alt="Line" src="https://c.animaapp.com/a0hzXRiM/img/line-.svg" />
              <div className="text-wrapper-4">Główne założenia programu:</div>
            </div>
          </div>
          <a href="#" class="more-info-button">
              <div className="text-wrapper-5">Dowiedz się więcej</div>
          </a>
        </div>
        <div className="text-wrapper-6">© 2024 AMM Script</div>
        <div className="text-wrapper-7">AMM Script</div>
      </div>
    </div>
  );
};
export default AboutPage;