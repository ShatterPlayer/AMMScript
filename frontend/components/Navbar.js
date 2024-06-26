import React from "react";
import "./Navbar.css";
import '../app/globals.css'

export const Navbar = () => {
  return (
    <div className="Navbar">
        <div className="overlap">
          <a href="/" className="home-button">
            <div className="overlap-group">
              <div className="text-wrapper">Home</div>
            </div>
          </a>
          <a href="/AboutPage" className="about-button">
            <div className="div-wrapper">
              <div className="text-wrapper-2">About</div>
            </div>
          </a>
          <a href="/infoPage" className="info-button">
            <div className="overlap-2">
              <div className="text-wrapper-3">Info</div>
            </div>
          </a>
        </div>
    </div>
  );
};
export default Navbar;
