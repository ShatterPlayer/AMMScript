import React from "react";
import "./infoPage.css";
import '../app/globals.css'
import Navbar from "../components/Navbar";


export const infoPage = () => {
  return (
    <div className="Info-page">
      <div className="div">
       <Navbar/>
        <div className="overlap-3">
          <div className="background">
            <div className="overlap-4">
             <div className="rectangle"/>
              <div className="rectangle-2"/>
              <img className="line" alt="Line" src="https://c.animaapp.com/a0hzXRiM/img/line-.svg" />
              <div className="text-wrapper-4">Informacje:</div>
              <div className="text-wrapper-8">
              <div className="text-wrapper-8">
                <div>1. Github</div>
                <div>2. Dokumentacja</div>
              </div>
              </div>
            </div>
          </div>
        </div>
        <div className="text-wrapper-6">© 2024 AMM Script</div>
        <div className="text-wrapper-7">AMM Script</div>
      </div>
    </div>
  );
};
export default infoPage;