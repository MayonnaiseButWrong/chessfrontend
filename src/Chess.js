import './Chess.css'
import {Text, StyleSheet} from 'react-native';
import React, {useState} from 'react';
import { Chessboard } from "react-chessboard";
import {toFEN,toTuple,toDict,toUnicode} from './translations.js'
import {MoveSuccessful,isCheckmate} from './Chessengine';

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

//add checkamte
//fix king movement
//fix moving a piece on the board in general



const styles = StyleSheet.create({
    last_moves_text: {
        fontFamily: 'Raleway',
        fontSize: 25,
        fontWeight: 'light',
        position: 'center',
        color:'#dddddd'
    },
    black_pieces_taken_text: {
        fontFamily: 'Raleway',
        fontSize: 25,
        fontWeight: 'light',
        position: 'center',
        color:'#dddddd'
    },
    white_pieces_taken_text: {
        fontFamily: 'Raleway',
        fontSize: 25,
        fontWeight: 'light',
        position: 'center',
        color:'#dddddd'
    },
})

const ChessFrontEnd = () => {
    var originalPieces=FindPieces(startingLayout)
    const originalBlackPieces=originalPieces[0]
    const originalWhitePieces=originalPieces[1]
    var currentLayout = startingLayout;
    var currentString = toDict(currentLayout);
    var currentMove = [];
    var turn = 'W';
    var previosMoves = [];
    var previosMove=[]
    var LastMovesText=''
    var LastMovesList=[]
    var whitePiecesTakenText=''
    var whitePiecesTakenList=[]
    var blackPiecesTakenText=''
    var blackPiecesTakenList=[]
    var currentPiece=''
    var editing=false
    
    function FindPieces (currentLayout) {
        let blackPieces=[]
        let whitePieces=[]
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                if (!(currentLayout[j][i]==='MT')) {
                    if (currentLayout[j][i][0]==='B') {
                        blackPieces.push(currentLayout[j][i])
                    } else {
                        whitePieces.push(currentLayout[j][i])
                    }
                }
            }
        }
        return [blackPieces,whitePieces]
    }
    
    function onDrop (fromSquare, toSquare, piece) {
        console.log(fromSquare,toSquare)
        let MoveSuccesfulTuple = [];
        fromSquare = String(fromSquare).toUpperCase();
        toSquare = String(toSquare).toUpperCase();
        previosMove=currentMove
        currentMove=[fromSquare,toSquare]
        console.log('currentMove',currentMove)
        if(previosMove.length>1) {
            let inverseMove=[previosMove[1],previosMove[0]]
            if (currentLayout[toTuple(inverseMove[0])[1]][toTuple(inverseMove[0])[0]][0]===turn&&fromSquare===inverseMove[0]&&toSquare===inverseMove[1]) {
                currentPiece=piece
                move()
                LastMovesList=LastMovesList.shift()
                return true
            };
            if(editing===true) {
                fromSquare=currentMove[0]
            }
        };
        MoveSuccesfulTuple=MoveSuccessful(fromSquare,toSquare,currentLayout,turn,previosMoves);
        console.log(fromSquare,toSquare)
        if (MoveSuccesfulTuple[0]===true) {
            currentPiece=piece
            currentMove=[fromSquare,toSquare]
            console.log('currentMove',currentMove)
            move()
            if (editing===true) {
                LastMovesList[0]=toUnicode(currentPiece)+' => '+currentMove[1]
            } else {
                LastMovesList=LastMovesList.push()
                editing=true
            }
            LastMovesText=LastMovesList.toString()
            changelast_moves_text(LastMovesText)
            return true
        } else {return false;};
    }
    
    function move () {
        let boardCopy=currentLayout
        let currentPosition=[]
        let fromSquare=currentMove[0]
        let toSquare=currentMove[1]
        console.log(toSquare)
        console.log(fromSquare)
        console.log(toTuple(toSquare))
        console.log(toTuple(fromSquare))
        if (currentMove.length===3) {
            if (currentMove[3][0][1]==='Q'||currentMove[3][0][1]==='B'||currentMove[3][0][1]==='R'||currentMove[3][0][1]==='N'){
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]]=currentMove[3][0]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]='MT'
                if (currentMove[3].length>1) {
                    for (let move = 1; move < currentMove[3].length; move++) {
                        currentPosition=toTuple(currentMove[3][move])
                        boardCopy[currentPosition[1]][currentPosition[0]]='MT'
                    }
                }
            } else {
                for (let move = 0; move < currentMove[3].length; move++) {
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

    const [last_moves_text, setlast_moves_text] = useState("Bird's Nest");
    const changelast_moves_text = (text) => {setlast_moves_text(text);}

    const [black_pieces_taken_text, setblack_pieces_taken_text] = useState("Bird's Nest");
    const changeblack_pieces_taken_text = (text) => {setblack_pieces_taken_text(text);}

    const [white_pieces_taken_text, setwhite_pieces_taken_text] = useState("Bird's Nest");
    const changewhite_pieces_taken_text = (text) => {setwhite_pieces_taken_text(text);}

    function selectMove() {
        let currentPieces=[]
        let currentBlackPieces=[]
        let currentWhitePieces=[]
        let temp=[]
        console.log('skdfjbvhfjk',currentMove)
        if (currentMove.length>1) {
            turn=(turn==='W')? 'B':'W';
            console.log(turn)
            previosMoves.push(currentMove);
            currentMove=[];
        };
        currentPieces=FindPieces(currentLayout)
        currentBlackPieces=currentPieces[0]
        currentWhitePieces=currentPieces[1]
        for (let blackPieces = 0; blackPieces < originalBlackPieces.length; blackPieces++) {
            for (let pieces = 0; pieces < currentBlackPieces.length; pieces++) {
                if (!(originalBlackPieces[blackPieces]===currentBlackPieces[pieces])) {
                    whitePiecesTakenList.push(originalBlackPieces[blackPieces])
                }
            }
        }
        for (let whitePieces = 0; whitePieces < originalWhitePieces.length; whitePieces++) {
            for (let pieces = 0; pieces < currentWhitePieces.length; pieces++) {
                if (!(originalWhitePieces[whitePieces]===currentWhitePieces[pieces])) {
                    blackPiecesTakenList.push(originalWhitePieces[whitePieces])
                }
            }
        }
        whitePiecesTakenList.sort()
        blackPiecesTakenList.sort()
        for (let elements = 0; elements < whitePiecesTakenList.length; elements++) {
            temp.push(toUnicode(whitePiecesTakenList[elements]))
        }
        whitePiecesTakenList=temp
        for (let elements = 0; elements < blackPiecesTakenList.length; elements++) {
            temp.push(toUnicode(blackPiecesTakenList[elements]))
        }
        blackPiecesTakenList=temp
        whitePiecesTakenText=whitePiecesTakenList.toString()
        blackPiecesTakenText=blackPiecesTakenList.toString()
        changewhite_pieces_taken_text(whitePiecesTakenText)
        changeblack_pieces_taken_text(blackPiecesTakenText)
        if (isCheckmate(currentLayout,turn,previosMoves)===true) {
            console.log('checkamte')
        }
    };

    //history.pushState(null, document.title, location.href);
    //window.addEventListener('popstate', function (event)
    //{
    //    const leavePage = confirm("you want to go ahead ?");
    //    if (leavePage) {
    //    history.back(); 
    //    } else {
    //        history.pushState(null, document.title, location.href);
    //    }  
    //});
    
    console.log(currentString,'1',currentMove)
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
                <span className='selet_move_button'>
                    <button className='type2' onClick={selectMove}>Select Move</button>
                </span>

                <span className='last_moves'>
                    <h2 className='last_moves_header'>Last Moves</h2>
                    <Text style={styles.last_moves_text} className='last_moves_text' id='p1'>{last_moves_text}</Text>
                </span>

                <span className='black_pieces_taken'>
                    <h2 className='black_pieces_taken_header'>Black Pieces Taken</h2>
                    <Text style={styles.black_pieces_taken_text} className='black_pieces_taken_text' id='black_pieces_taken_text'>{black_pieces_taken_text}</Text>
                </span>

                <span className='white_pieces_taken'>
                    <h2 className='white_pieces_taken_header'>White Pieces</h2>
                    <Text style={styles.white_pieces_taken_text} className='white_pieces_taken_text' id ='white_pieces_taken_text'>{white_pieces_taken_text}</Text>
                </span>
                <span className= 'disclaimer'>
                    <p className='disclaimer_text'>asifhkjlkvm;lsfrjhgiwuqehojpkdfl</p>
                </span>
            </div>
        </div>
    </div>
    );
};

export default ChessFrontEnd;