import React from "react";
import "./aboutPage.css";
import '../app/globals.css'
import Navbar from "../components/Navbar";


export const aboutPage = () => {
  return (
    <div className="About-page">
      <div className="div">
        <Navbar/>
        <div className="overlap-3">
          <div className="background">
            <div className="overlap-4">
             <div className="rectangle"/>
              <div className="rectangle-2"/>
              <div className="code-input"/>
              <img className="line" alt="Line" src="https://c.animaapp.com/a0hzXRiM/img/line-.svg" />
              <div className="text-wrapper-4">Główne założenia:</div>
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
export default aboutPage;