import './OptionsPage.css';
import React from 'react';
import {Link} from 'react-router-dom'

const OptionsPage = () => {
    //const [contentType, setContentType] = React.useSyncExternalStore('p1');
    return (
      <div className="OptionsPage">
        <h1>Chess</h1>
        <Link to= "/ChessGame"><div className="container"><button> Daily Chess</button></div></Link>
        <div class="grid-container">
          <Link to= "/ChessGame"> <button>2 Player Normal Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button> 1 Player Normal Chess</button>                     </Link>  
          <Link to= "/ChessGame"> <button> 2 Player Fischer Random Chess</button>             </Link>
          <Link to= "/ChessGame"> <button> 1 Player Fischer Random Chess</button>             </Link>
          <Link to= "/ChessGame"> <button> 2 Player Transcendental Chess</button>             </Link>
          <Link to= "/ChessGame"> <button> 1 Player Transcendental Chess</button>             </Link>
          <Link to= "/ChessGame"> <button> 2 Player Upside Down Chess</button>                </Link>
          <Link to= "/ChessGame"> <button> 1 Player Upside Down Chess</button>                </Link>  
          <Link to= "/ChessGame"> <button> 2 Player Weak! Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button> 1 Player Weak! Chess</button>                      </Link>
          <Link to= "/ChessGame"> <button> 2 Player Charge Of The Light Brigade Chess</button></Link> 
          <Link to= "/ChessGame"> <button> 1 Player Charge Of The Light Brigade Chess</button></Link>
          <Link to= "/ChessGame"> <button> 2 Player Peasants' Revolt Chess</button>           </Link>
          <Link to= "/ChessGame"> <button> 1 Player Peasants' Revolt Chess</button>           </Link> 
          <Link to= "/ChessGame"> <button> 2 Player EndGame Chess</button>                    </Link>
          <Link to= "/ChessGame"> <button> 1 Player EndGame Chess</button>                    </Link>   
        </div> 
      </div>
    );
  };


export default OptionsPage;