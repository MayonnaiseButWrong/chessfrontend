import './OptionsPage.css';
import React from 'react';
import {Link} from 'react-router-dom'
var choice = 0;
function changePage (state) {
        choice=state
};

//document.getElementById("button 1").addEventListener("click", changePage(1));
//document.getElementById("button 2").addEventListener("click", changePage(2));
//document.getElementById("button 3").addEventListener("click", changePage(3));
//document.getElementById("button 4").addEventListener("click", changePage(4));
//document.getElementById("button 5").addEventListener("click", changePage(5));
//document.getElementById("button 6").addEventListener("click", changePage(6));
//document.getElementById("button 7").addEventListener("click", changePage(7));
//document.getElementById("button 8").addEventListener("click", changePage(8));
//document.getElementById("button 9").addEventListener("click", changePage(9));
//document.getElementById("button 10").addEventListener("click", changePage(10));
//document.getElementById("button 11").addEventListener("click", changePage(11));
//document.getElementById("button 12").addEventListener("click", changePage(12));
//document.getElementById("button 13").addEventListener("click", changePage(13));
//document.getElementById("button 14").addEventListener("click", changePage(14));
//document.getElementById("button 15").addEventListener("click", changePage(15));
//document.getElementById("button 16").addEventListener("click", changePage(16));
//document.getElementById("button 17").addEventListener("click", changePage(17));

const OptionsPage = () => {
    return (
      <div className="OptionsPage">
        <h1>Chess</h1>
        <Link to= "/ChessGame"><div className="container"><button id="button 1"> Daily Chess</button></div>    </Link>
        <div class="grid-container">
          <Link to= "/ChessGame"> <button id="button 2"> 2 Player Normal Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button id="button 3"> 1 Player Normal Chess</button>                      </Link>  
          <Link to= "/ChessGame"> <button id="button 4"> 2 Player Fischer Random Chess</button>              </Link>
          <Link to= "/ChessGame"> <button id="button 5"> 1 Player Fischer Random Chess</button>              </Link>
          <Link to= "/ChessGame"> <button id="button 6"> 2 Player Transcendental Chess</button>              </Link>
          <Link to= "/ChessGame"> <button id="button 7"> 1 Player Transcendental Chess</button>              </Link>
          <Link to= "/ChessGame"> <button id="button 8"> 2 Player Upside Down Chess</button>                 </Link>
          <Link to= "/ChessGame"> <button id="button 9"> 1 Player Upside Down Chess</button>                 </Link>  
          <Link to= "/ChessGame"> <button id="button 10"> 2 Player Weak! Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button id="button 11"> 1 Player Weak! Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button id="button 12"> 2 Player Charge Of The Light Brigade Chess</button></Link> 
          <Link to= "/ChessGame"> <button id="button 13"> 1 Player Charge Of The Light Brigade Chess</button></Link>
          <Link to= "/ChessGame"> <button id="button 14"> 2 Player Peasants' Revolt Chess</button>           </Link>
          <Link to= "/ChessGame"> <button id="button 15"> 1 Player Peasants' Revolt Chess</button>           </Link> 
          <Link to= "/ChessGame"> <button id="button 16"> 2 Player EndGame Chess</button>                    </Link>
          <Link to= "/ChessGame"> <button id="button 17"> 1 Player EndGame Chess</button>                    </Link>   
        </div>
      </div>
    );
  };

export {OptionsPage, choice};