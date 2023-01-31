import './Chess.css'
import { Chessboard } from "react-chessboard";
import toFen from './listToFEN.js'
import MoveSuccessful from './Chessengine';

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

//each move is a list that has 3 components, from, to, and a tuple containing information about if its an enpassant, promotion or nothing. if the thid component is empt then its a normal move.

var currentLayout = startingLayout
var currentString = toFen(currentLayout);
var currentMove = []
var targetSquare = ''
var currentPiece = ''

function toTuple(InputCoOrdinates) {
    const letters=['A','B','C','D','E','F','G','H']
    return [Number(letters.indexOf(InputCoOrdinates[0])),8-Number(InputCoOrdinates[1])]
}

function onDrop (fromSquare, toSquare, piece) {
    console.log(fromSquare,toSquare)
    let MoveSuccesfulTuple = [];
    fromSquare = String(fromSquare).toUpperCase();
    toSquare = String(toSquare).toUpperCase();
    MoveSuccesfulTuple=MoveSuccessful(fromSquare,toSquare,currentLayout);
    console.log(fromSquare,toSquare)
    if (MoveSuccesfulTuple[0]===true) {
        move(fromSquare,toSquare)
        currentPiece=piece
        currentMove=MoveSuccesfulTuple[1]
        console.log('bhkjvgfytuygi')
        return true
    } else {return false;};
}

function move (fromSquare,toSquare) {
    let boardCopy=currentLayout
    console.log(toSquare)
    console.log(fromSquare)
    console.log(toTuple(toSquare))
    console.log(toTuple(fromSquare))
    boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]]=boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
    boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]='MT'
    currentLayout=boardCopy
    console.log(currentLayout.toString())
    currentString=toFen(currentLayout)
    console.log(currentString)
}

const ChessFrontEnd = () => {

    console.log(currentString)
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

export default ChessFrontEnd;