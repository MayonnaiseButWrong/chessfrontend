import './Chess.css'
import {Link} from 'react-router-dom'
import { Chessboard } from "react-chessboard";
import Chess from 'chess.js';

//<Link to='/'><button onClick='ChessFrontEnd(2,1)'> Quit / New game</button></Link>

const startingLayout = [
    ['BR','BN','BB','BQ','BK','BB','BN','BR'],
    ['BP','BP','BP','BP','BP','BP','BP','BP'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['WP','WP','WP','WP','WP','WP','WP','WP'],
    ['WR','WN','WB','WQ','WK','WB','WN','WR']
    ];

let startingString = (InputList=startingLayout) => {
    var output ='';
    var count =0;
    for (let j = 0; j < InputList.length; j++) {
        for (let i = 0; i < InputList[i].length; i++) {
            count=0
            while (InputList[j][i+count][0]==='M') {
                count++
            }
            if (InputList[j][i][0]==='W') {
                output += InputList[j][i][1];
            }
            else {
                output += InputList[j][i][1].toLowerCase();
            };
            if (count>0) {
                i+=count
                output += count
            }
        };
        output += '/';
    };
    return output;
};

let chessBoardWidth = (w=window.innerWidth,h=window.innerHeight) => {
    if (h>w) {return Math.round(0.6*h)}
    else {return Math.round(0.6*w)}
};

const ChessFrontEnd = () => {
    return(
    <div className="ChessFrontEnd">
        <h1>Chess</h1>
        <div className="grid-container1">
            <span className= 'boarderleft'></span>
            <div className='chessboard'>
                <Chessboard //using an api to display the chessboard on screen.It isn't feesable for me to make this part from sctach in the time period given for this project
                 id='board1' //the api is open source an cusomisable, allowing me to make the board look anw function the way I want it too
                 position={startingLayout} 
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

            <div className='details'>
                <span className='selet-move-button'>
                    <button className='type2'>Select Move</button>
                </span>

                <span className='last-moves'>
                    <h2 className='last-moves-header'>Last Moves</h2>
                    <p className='last-moves-text'>startingString</p>
                </span>

                <span className='black-pieces-taken'>
                    <h2 className='black-pieces-taken-header'>Black Pieces Taken</h2>
                    <p className='black-pieces-taken-text'>dfbgdfvyjh</p>
                </span>

                <span className='white-pieces-taken'>
                    <h2 className='white-pieces-taken-header'>White Pieces</h2>
                    <p className='white-pieces-taken-text'>sghnyjukyjt</p>
                </span>

                <span className= 'boarderright'></span>

                <span className= 'disclaimer'>
                    <p className='disclaimer-text'>asifhkjlkvm;lsfrjhgiwuqehojpkdfl</p>
                </span>
            </div>
        </div>
    </div>
    );
};

export default ChessFrontEnd;