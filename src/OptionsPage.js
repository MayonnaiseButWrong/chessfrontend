import './OptionsPage.css';
import React from 'react';
import {Link} from 'react-router-dom'

var choice = 0;

const OptionsPage = () => {
    //const [contentType, setContentType] = React.useSyncExternalStore('p1');
    return (
      <div className="OptionsPage">
        <h1>Chess</h1>
        <Link to= "/ChessGame"><div className="container"><button> Daily Chess</button></div></Link>
        <div class="grid-container">
          <Link to= "/ChessGame"> <button onClick={choice=2}> 2 Player Normal Chess</button>          </Link>
          <Link to= "/ChessGame"> <button onClick={choice=3}> 1 Player Normal Chess</button>                     </Link>  
          <Link to= "/ChessGame"> <button onClick={choice=4}> 2 Player Fischer Random Chess</button>             </Link>
          <Link to= "/ChessGame"> <button onClick={choice=5}> 1 Player Fischer Random Chess</button>             </Link>
          <Link to= "/ChessGame"> <button onClick={choice=6}> 2 Player Transcendental Chess</button>             </Link>
          <Link to= "/ChessGame"> <button onClick={choice=7}> 1 Player Transcendental Chess</button>             </Link>
          <Link to= "/ChessGame"> <button onClick={choice=8}> 2 Player Upside Down Chess</button>                </Link>
          <Link to= "/ChessGame"> <button onClick={choice=9}> 1 Player Upside Down Chess</button>                </Link>  
          <Link to= "/ChessGame"> <button onClick={choice=10}> 2 Player Weak! Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button onClick={choice=11}> 1 Player Weak! Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button onClick={choice=12}> 2 Player Charge Of The Light Brigade Chess</button></Link> 
          <Link to= "/ChessGame"> <button onClick={choice=13}> 1 Player Charge Of The Light Brigade Chess</button></Link>
          <Link to= "/ChessGame"> <button onClick={choice=14}> 2 Player Peasants' Revolt Chess</button>           </Link>
          <Link to= "/ChessGame"> <button onClick={choice=15}> 1 Player Peasants' Revolt Chess</button>           </Link> 
          <Link to= "/ChessGame"> <button onClick={choice=16}> 2 Player EndGame Chess</button>                    </Link>
          <Link to= "/ChessGame"> <button onClick={choice=17}> 1 Player EndGame Chess</button>                    </Link>   
        </div> 
      </div>
    );
  };

const page = choice;

export {OptionsPage, page};