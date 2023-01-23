import './Chess.css'
import {Link} from 'react-router-dom'
import { Chessboard } from "react-chessboard";
import Chess from 'chess.js';

//<Link to='/'><button onClick='ChessFrontEnd(2,1)'> Quit / New game</button></Link>
//customBoardStyle={
//    borderRadius: '15px',
//    boxShadow: '0 5px 15px rgba(0, 0, 0, 0.5'
//  }
// customDarkSquareStyle={backgroundColor: '#B58863' }
// customLightSquareStyle={backgroundColor: '#B58863'}
// customDropSquareStyle={ boxShadow: 'inset 0 0 1px 6px rgba(255,255,255,0.75)' }
// customPremoveDarkSquareStyle={ backgroundColor: '#A42323' }
// customPreMoveLightSquareStyle={ backgroundColor: '#BD2828' }
// 


const startingLayout = [
    [],
    [],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    [],
    []
    ];

let chessBoardWidth = (w=window.innerWidth,h=window.innerHeight) => {
    if (h>w) {return Math.round(0.6*w)}
    else {return Math.round(0.6*h)}
};

const ChessFrontEnd = () => {
    return(
    <div className="ChessFrontEnd">
        <h1>Chess</h1>
        <div class="grid-container1">
            <div class= 'boarderleft'></div>
            <div class='chessboard'>
            <Chessboard //using an api to display the chessboard on screen.It isn't feesable for me to make this part from sctach in the time period given for this project
            id='board1' //the api is open source an cusomisable, allowing me to make the board look anw function the way I want it too
             position={'start'} 
             animationDuration='300'
             areArrowsAllowed='true'
             arePiecesDraggable='true'
             arePremovesAllowed='true'
             boardOrientation='white'
             boardwidth={chessBoardWidth}
             clearPremovesOnRightClick='true'
             customArrowColor='#eda215'
             />
            </div>

            <div class='selet-move-button'>
                <button class='type2'>Select Move</button>
            </div>

            <div class='last-moves'>
                <h2 class='last-moves-header'>Last Moves</h2>
                <p class='last-moves-text'>efwasdf</p>
            </div>

            <div class='black-pieces-taken'>
                <h2 class='black-pieces-taken-header'>Black Pieces Taken</h2>
                <p class='black-pieces-taken-text'>dfbgdfvyjh</p>
            </div>

            <div class='white-pieces-taken'>
                <h2 class='white-pieces-taken-header'>White Pieces</h2>
                <p class='white-pieces-taken-text'>sghnyjukyjt</p>
            </div>

            <div class= 'boarderright'></div>

            <div class= 'disclaimer'>
                <p class='disclaimer-text'>asifhkjlkvm;lsfrjhgiwuqehojpkdfl</p>
            </div>
        </div>
    </div>
    );
};

export default ChessFrontEnd;