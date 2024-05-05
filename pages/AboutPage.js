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
              <div className="text-wrapper-8">
              <div className="text-wrapper-8">
                <div>1. Prostota składni - AMM Script został zaprojektowany w sposób umożliwiający intuicyjną naukę dla początkujących programistów.</div>
                <div>2. Zmienne - Język obsługuje zmienne, które mogą przechowywać różne typy danych. W przykładzie stosujemy set dla przypisania wartości do zmiennych: set x 10</div>
                <div>set y “Hello World!”</div>
                <div>Wypisanie:</div>
                <div>print x</div>
                <div>print y</div>
                <div>3. Obsługa błędów - na przykład obsługa błędów dla przypadku kiedy użytkownik próbuje odwołać się do niezidentyfikowanej zmiennej</div>
                <div>4. Modularność - użytkownicy będą mogli dodawać nowe funkcje, instrukcje lub typy danych, żeby język był lepiej przystosowany do różnych zastosowań</div>
                <div>5. Czytelność - kod łatwy do zrozumienia i analizowania</div>
              </div>
              </div>
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