import './OptionsPage.css';
import React from 'react';
import { Link } from 'react-router-dom'

const OptionsPage = () => {
  return (
    <div className="OptionsPage">
      <h1>Chess</h1>
      <div className="grid-container">
        <div className='boarderleft'></div>
        <div className='topbutton'><Link to="/DailyChess"><button id="button 1"> Daily Chess</button>              </Link></div>
        <div><Link to="/TwoPlayerNormalChess"> <button id="button 2"> 2 Player Normal Chess</button>                      </Link></div>
        <div><Link to="/OnePlayerNormalChess"> <button id="button 3"> 1 Player Normal Chess</button>                      </Link></div>
        <div><Link to="/TwoPlayerFischerRandomChess"> <button id="button 4"> 2 Player Fischer Random Chess</button>              </Link></div>
        <div><Link to="/OnePlayerFischerRandomChess"> <button id="button 5"> 1 Player Fischer Random Chess</button>              </Link></div>
        <div><Link to="/TwoPlayerTranscendentalChess"> <button id="button 6"> 2 Player Transcendental Chess</button>              </Link></div>
        <div><Link to="/OnePlayerTranscendentalChess"> <button id="button 7"> 1 Player Transcendental Chess</button>              </Link></div>
        <div><Link to="/TwoPlayerUpsideDownChess"> <button id="button 8"> 2 Player Upside Down Chess</button>                 </Link></div>
        <div><Link to="/OnePlayerUpsideDownChess"> <button id="button 9"> 1 Player Upside Down Chess</button>                 </Link></div>
        <div><Link to="/TwoPlayerWeakChess"> <button id="button 10"> 2 Player Weak! Chess</button>                      </Link></div>
        <div><Link to="/OnePlayerWeakChess"> <button id="button 11"> 1 Player Weak! Chess</button>                      </Link></div>
        <div><Link to="/TwoPlayerChargeOfTheLightBrigadeChess"> <button id="button 12"> 2 Player Charge Of The Light Brigade Chess</button></Link></div>
        <div><Link to="/OnePlayerChargeOfTheLightBrigadeChess"> <button id="button 13"> 1 Player Charge Of The Light Brigade Chess</button></Link></div>
        <div><Link to="/TwoPlayerPeasantsRevoltChess"> <button id="button 14"> 2 Player Peasants' Revolt Chess</button>           </Link></div>
        <div><Link to="/OnePlayerPeasantsRevoltChess"> <button id="button 15"> 1 Player Peasants' Revolt Chess</button>           </Link></div>
        <div><Link to="/TwoPlayerEndGameChess"> <button id="button 16"> 2 Player EndGame Chess</button>                    </Link></div>
        <div><Link to="/OnePlayerEndGameChess"> <button id="button 17"> 1 Player EndGame Chess</button>                    </Link></div>
        <div className='boarderright'></div>
        <div className='disclaimer'>
          <p className='disclaimer-text'>
            Data about the chess games, such as what moves were made and in what order, are stored so that the AI can learn and get better at chess. No data about the user is stored.
          </p>
        </div>
      </div>
    </div>
  );
};

export default OptionsPage;