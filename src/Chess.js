import './Chess.css'
import {Link} from 'react-router-dom'
import { Chessboard } from "react-chessboard";
import Chess from 'chess.js';

//<Link to='/'><button onClick='ChessFrontEnd(2,1)'> Quit / New game</button></Link>

 
//const translationIndex = {
//    
//}
//
//const startingLayout = [
//    ['BR','BH','BB','BQ','BK','BB','BH','BR'],
//    ['BP','BP','BP','BP','BP','BP','BP','BP'],
//    ['MT','MT','MT','MT','MT','MT','MT','MT'],
//    ['MT','MT','MT','MT','MT','MT','MT','MT'],
//    ['MT','MT','MT','MT','MT','MT','MT','MT'],
//    ['MT','MT','MT','MT','MT','MT','MT','MT'],
//    ['WP','WP','WP','WP','WP','WP','WP','WP'],
//    ['WR','WH','WB','WQ','WK','WB','WH','WR']
//    ];
//
//let startingString = (InputList=startingLayout) => {
//    for (let i = 0; i < InputList.length; i++) {
//        InputList[i]
//    }
//}

let chessBoardWidth = (w=window.innerWidth,h=window.innerHeight) => {
    if (h>w) {return Math.round(0.6*h)}
    else {return Math.round(0.6*w)}
};

const ChessFrontEnd = () => {
    return(
    <div className="ChessFrontEnd">
        <h1>Chess</h1>
        <div class="grid-container1">
            <span class= 'boarderleft'></span>
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
                 snapToCursor='true'
                 showBoardNotation='true'
                 customArrowColor='#eda215'
                 customBoardStyle={{
                     borderRadius: '15px',
                     boxShadow: '0 5px 15px rgba(0, 0, 0, 0.5'
                 }}
                 customDarkSquareStyle={{backgroundColor: '#1c1c1c'}}
                 customLightSquareStyle={{backgroundColor: '#d6d6d6'}}
                 customDropSquareStyle={{boxShadow: 'inset 0 0 1px 6px rgba(255,255,255,0.75)' }}
                 customPremoveDarkSquareStyle={{backgroundColor: '#470a61'}}
                 customPremoveLightSquareStyle={{backgroundColor: '#6c4080'}}
                 />
            </div>

            <div class='details'>
                <span class='selet-move-button'>
                    <button class='type2'>Select Move</button>
                </span>

                <span class='last-moves'>
                    <h2 class='last-moves-header'>Last Moves</h2>
                    <p class='last-moves-text'>efwasdf</p>
                </span>

                <span class='black-pieces-taken'>
                    <h2 class='black-pieces-taken-header'>Black Pieces Taken</h2>
                    <p class='black-pieces-taken-text'>dfbgdfvyjh</p>
                </span>

                <span class='white-pieces-taken'>
                    <h2 class='white-pieces-taken-header'>White Pieces</h2>
                    <p class='white-pieces-taken-text'>sghnyjukyjt</p>
                </span>

                <span class= 'boarderright'></span>

                <span class= 'disclaimer'>
                    <p class='disclaimer-text'>asifhkjlkvm;lsfrjhgiwuqehojpkdfl</p>
                </span>
            </div>
        </div>
    </div>
    );
};

export default ChessFrontEnd;