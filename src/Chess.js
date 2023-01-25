import './Chess.css'
import {Link} from 'react-router-dom'
import { Chessboard } from "react-chessboard";
import { Chess } from 'chess.js';
import toFen from './listToFEN.js'

//<Link to='/'><button onClick='ChessFrontEnd(2,1)'> Quit / New game</button></Link>

var startingLayout = [
    ['BR','BN','BB','BQ','BK','BB','BN','BR'],
    ['BP','BP','BP','BP','BP','BP','BP','BP'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['WP','WP','WP','WP','WP','WP','WP','WP'],
    ['WR','WN','WB','WQ','WK','WB','WN','WR']
    ];



const ChessFrontEnd = () => {

    var startingString = toFen(startingLayout);

    function generateQMoves(){
        var moves=[];
        for (let i = 0; i < 10; i++) {
            moves.append([i,0]);
            moves.append([-i,0]);
            moves.append([0,i]);
            moves.append([0,-i]);
            moves.append([i,i]);
            moves.append([i,-i]);
            moves.append([-i,i]);
            moves.append([-i,-i]);
        };
        return moves
    }

    //setTimeout(() => {
    //    setString()
    // }, 2000);
//
    //function setString () {
    //startingString = toFen([
    //    ['BR','BN','BB','BQ','BK','BB','BN','BR'],
    //    ['BP','BP','BP','BP','BP','BP','BP','BP'],
    //    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    //    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    //    ['MT','MT','MT','MT','WP','MT','MT','MT'],
    //    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    //    ['WP','WP','WP','WP','MT','WP','WP','WP'],
    //    ['WR','WN','WB','WQ','WK','WB','WN','WR']
    //    ])
    //    console.log(startingString)
    //    return startingString
    //}
    //console.log(startingString)
    
    var currentLayout=[
        ['BR','BN','BB','BQ','BK','BB','BN','BR'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','WP','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['WP','WP','WP','WP','MT','WP','WP','WP'],
        ['WR','WN','WB','WQ','WK','WB','WN','WR']
        ];

    function generatePossibleMoves (currentLayout) {
        const moveVectors = {
            'Q': Qmoves=generateQMoves,
            'K': [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[0,-1]],
            'B': Bmoves=generateBMoves,
            'N': [],
            'R': [],
            'P': []
        }
    }


    function OnClick (square){
        console.log('here2')
    }

    return(
    <div className="ChessFrontEnd">
        <h1>Chess</h1>
        <div className="grid-container1">
            <div className='chessboard'>
                <Chessboard //using an api to display the chessboard on screen.It isn't feesable for me to make this part from sctach in the time period given for this project
                 id='board1' //the api is open source an cusomisable, allowing me to make the board look anw function the way I want it too
                 position={startingString} 
                 customArrowColor='#eda215'
                 customBoardStyle={{
                     borderRadius: '15px',
                     boxShadow: '0 5px 15px rgba(0, 0, 0, 0.5)'
                 }}
                 customDarkSquareStyle={{backgroundColor: '#1f1f1f'}}
                 customLightSquareStyle={{backgroundColor: '#d6d6d6'}}
                 customDropSquareStyle={{boxShadow: 'inset 0 0 1px 6px rgba(255,255,255,0.75)' }}
                 customPremoveDarkSquareStyle={{backgroundColor: '#470a61'}}
                 customPremoveLightSquareStyle={{backgroundColor: '#6c4080'}}
                 onPieceClick={OnClick}
                 />
            </div>

            <div className='details'>
                <span className='selet-move-button'>
                    <button className='type2'>Select Move</button>
                </span>

                <span className='last-moves'>
                    <h2 className='last-moves-header'>Last Moves</h2>
                    <p className='last-moves-text' id='p1'>iuvbhlijbvgctigyh</p>
                </span>

                <span className='black-pieces-taken'>
                    <h2 className='black-pieces-taken-header'>Black Pieces Taken</h2>
                    <p className='black-pieces-taken-text' id='black-pieces-taken-text'>dfbgdfvyjh</p>
                </span>

                <span className='white-pieces-taken'>
                    <h2 className='white-pieces-taken-header'>White Pieces</h2>
                    <p className='white-pieces-taken-text' id ='white-pieces-taken-text'>sghnyjukyjt</p>
                </span>
                <span className= 'disclaimer'>
                    <p className='disclaimer-text'>asifhkjlkvm;lsfrjhgiwuqehojpkdfl</p>
                </span>
            </div>
        </div>
    </div>
    );
};

//const timeout = setTimeout(setString,10000);
//
//window.onload = setString ()
//
//function setString () {
//    document.getElementById("p1").innerHTML = 'sfgdgrdthdf'
//}

export default ChessFrontEnd;