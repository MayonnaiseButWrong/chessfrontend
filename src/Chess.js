import './Chess.css'
import { Chessboard } from "react-chessboard";
import {toFEN,toTuple,toDict} from './translations.js'
import MoveSuccessful from './Chessengine';

var startingLayout = [
    ['BR','BN','BB','BQ','BK','BB','BN','BR'],
    ['BP','BP','BP','BP','BP','BP','BP','BP'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['MT','MT','MT','MT','WP','MT','MT','MT'],
    ['MT','MT','MT','MT','MT','MT','MT','MT'],
    ['WP','WP','WP','WP','MT','WP','WP','WP'],
    ['WR','WN','WB','WQ','WK','WB','WN','WR']
    ];

//each move is a list that has 3 components, from, to, and a tuple containing information about if its an enpassant, promotion or nothing. if the thid component is empt then its a normal move.

var currentLayout = startingLayout;
var currentString = toDict(currentLayout);
var currentMove = [];
var turn = 'W';
var previosMoves = [];

function selectMove() {
    console.log('skdfjbvhfjk')
    if (currentMove.length>1) {
        turn=(turn==='W')? 'B':'W';
        previosMoves.push(currentMove);
        currentMove=[];
    };
};

function onDrop (fromSquare, toSquare, piece) {
    console.log(fromSquare,toSquare)
    let MoveSuccesfulTuple = [];
    fromSquare = String(fromSquare).toUpperCase();
    toSquare = String(toSquare).toUpperCase();
    if(currentMove.length>1) {
        let inverseMove=[currentMove[1],currentMove[0]]
        if (currentLayout[toTuple(inverseMove[0])[1]][toTuple(inverseMove[0])[0]][0]==turn&&fromSquare===inverseMove[0]&&toSquare===inverseMove[1]) {
            currentPiece=piece
            currentMove=inverseMove
            move(currentMove)
            console.log('bhkjvgfytuygi')
            return true
        };
    };
    MoveSuccesfulTuple=MoveSuccessful(fromSquare,toSquare,currentLayout,turn,previosMoves);
    console.log(fromSquare,toSquare)
    if (MoveSuccesfulTuple[0]===true) {
        currentPiece=piece
        currentMove=MoveSuccesfulTuple[1]
        move(currentMove)
        console.log('bhkjvgfytuygi')
        return true
    } else {return false;};
}

function move (currentMove) {
    let boardCopy=currentLayout
    let currentPosition=[]
    fromSquare=currentMove[0]
    toSquare=currentMove[1]
    console.log(toSquare)
    console.log(fromSquare)
    console.log(toTuple(toSquare))
    console.log(toTuple(fromSquare))
    if (currentMove.length===3) {
        if (currentMove[3][0][1]==='Q'||currentMove[3][0][1]==='B'||currentMove[3][0][1]==='R'||currentMove[3][0][1]==='N'){
            boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]]=currentMove[3][0]
            boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]='MT'
            for (let move = 1; move < currentMoves[3].length; move++) {
                currentPosition=toTuple(currentMove[3][move])
                boardCopy[currentPosition[1]][currentPosition[0]]='MT'
            }
        } else {
            for (let move = 0; move < currentMoves[3].length; move++) {
                currentPosition=toTuple(currentMove[3][move])
                boardCopy[currentPosition[1]][currentPosition[0]]='MT'
            }
        };
    } else {
        boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]]=boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
        boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]='MT'
    };
    currentLayout=boardCopy
    console.log(currentLayout.toString())
    currentString=toDict(currentLayout)
    console.log(currentString,'2')
}

function currentPos (currentPosition) {
    console.log(currentPosition)
}

const ChessFrontEnd = () => {

    console.log(currentString,'1')
    return(
    <div className="ChessFrontEnd">
        <h1>Chess</h1>
        <div className="grid-container1">
            <div className='chessboard'>
                <Chessboard //using an api to display the chessboard on screen.It isn't feesable for me to make this part from sctach in the time period given for this project
                 id='board1' //the api is open source an cusomisable, allowing me to make the board look anw function the way I want it too
                 position={currentString}
                 showBoardNotation='true'
                 snapToCursor='true'
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
                 onPieceDrop={onDrop}
                 getPositionObject={currentPos}
                 />
            </div>

            <div className='details'>
                <span className='selet-move-button'>
                    <button className='type2' onClick={selectMove}>Select Move</button>
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

export default ChessFrontEnd;