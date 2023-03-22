import './OnePlayerPeasantsRevoltChess.css'
import { Text, StyleSheet } from 'react-native';
import React, { useState } from 'react';
import { Chessboard } from "react-chessboard";
import { toFEN, toTuple, toDict, toUnicode } from './translations.js'
import { MoveSuccessful, isCheckmate } from './Chessengine';

var startingLayout = [
    ['MT', 'BN', 'BN', 'MT', 'BK', 'MT', 'BN', 'MT'],
    ['MT', 'MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT'],
    ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
    ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
    ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
    ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['MT', 'MT', 'MT', 'MT', 'WK', 'MT', 'MT', 'MT']
];

//each move is a list that has 3 components, from, to, and a tuple containing information about if its an enpassant, promotion or nothing. if the thid component is empt then its a normal move.

//add checkamte
//fix king movement
//fix moving a piece on the board in general

var originalPieces = FindPieces(startingLayout)
const originalBlackPieces = originalPieces[0]
const originalWhitePieces = originalPieces[1]
var currentLayout = startingLayout;
var currentString = toDict(currentLayout);
var currentMove = [];
var turn = 'W';
var previosMoves = [];
var previosMove = []
var LastMovesText = ''
var LastMovesList = []
var whitePiecesTakenText = ''
var whitePiecesTakenList = []
var blackPiecesTakenText = ''
var blackPiecesTakenList = []
var currentPiece = ''
var moveDone = false
var buttonpressed = true

function FindPieces(currentLayout) {
    let blackPieces = { 'P': 0, 'K': 0, 'Q': 0, 'R': 0, 'B': 0, 'N': 0 }
    let whitePieces = { 'P': 0, 'K': 0, 'Q': 0, 'R': 0, 'B': 0, 'N': 0 }
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            if (!(currentLayout[j][i] === 'MT')) {
                if (currentLayout[j][i][0] === 'B') {
                    blackPieces[currentLayout[j][i][1]]++
                } else {
                    whitePieces[currentLayout[j][i][1]]++
                }
            }
        }
    }
    return [blackPieces, whitePieces]
}

const styles = StyleSheet.create({
    last_moves_text: {
        fontFamily: 'Raleway',
        fontSize: 25,
        fontWeight: 'light',
        position: 'center',
        color: '#dddddd'
    },
    black_pieces_taken_text: {
        fontFamily: 'Raleway',
        fontSize: 25,
        fontWeight: 'light',
        position: 'center',
        color: '#dddddd'
    },
    white_pieces_taken_text: {
        fontFamily: 'Raleway',
        fontSize: 25,
        fontWeight: 'light',
        position: 'center',
        color: '#dddddd'
    },
})

const OnePlayerPeasantsRevoltChess = () => {

    function currentPos(currentPosx) {
        console.log(currentPosx)
    }

    const [last_moves_text, setlast_moves_text] = useState("--");
    const changelast_moves_text = (text) => { setlast_moves_text(text); }

    const [black_pieces_taken_text, setblack_pieces_taken_text] = useState("--");
    const changeblack_pieces_taken_text = (text) => { setblack_pieces_taken_text(text); }

    const [white_pieces_taken_text, setwhite_pieces_taken_text] = useState("--");
    const changewhite_pieces_taken_text = (text) => { setwhite_pieces_taken_text(text); }



    //history.pushState(null, document.title, location.href);  do the same for a relode of the page
    //window.addEventListener('popstate', function (event)
    //{
    //    const leavePage = confirm("you want to go ahead ?");
    //    if (leavePage) {
    //    history.back(); 
    //    } else {
    //        history.pushState(null, document.title, location.href);
    //    }  
    //});

    function upadteCurrentString() {
        currentString = currentString
    }

    function selectMove() {
        let currentPieces = []
        let currentBlackPieces = []
        let currentWhitePieces = []
        let temp = []
        let checkmate = false
        console.log('skdfjbvhfjk', currentMove)
        if (moveDone === true) {

            whitePiecesTakenList = []
            blackPiecesTakenList = []
            currentPieces = FindPieces(currentLayout)
            currentBlackPieces = currentPieces[0]
            currentWhitePieces = currentPieces[1]

            if (currentBlackPieces['P'] < originalBlackPieces['P']) { blackPiecesTakenList.push('WP') }
            if (currentBlackPieces['Q'] < originalBlackPieces['Q']) { blackPiecesTakenList.push('WQ') }
            if (currentBlackPieces['K'] < originalBlackPieces['K']) { blackPiecesTakenList.push('WK') }
            if (currentBlackPieces['R'] < originalBlackPieces['R']) { blackPiecesTakenList.push('WR') }
            if (currentBlackPieces['B'] < originalBlackPieces['B']) { blackPiecesTakenList.push('WB') }
            if (currentBlackPieces['N'] < originalBlackPieces['N']) { blackPiecesTakenList.push('WN') }

            if (currentWhitePieces['P'] < originalWhitePieces['P']) { whitePiecesTakenList.push('BP') }
            if (currentWhitePieces['Q'] < originalWhitePieces['Q']) { whitePiecesTakenList.push('BQ') }
            if (currentWhitePieces['K'] < originalWhitePieces['K']) { whitePiecesTakenList.push('BK') }
            if (currentWhitePieces['R'] < originalWhitePieces['R']) { whitePiecesTakenList.push('BR') }
            if (currentWhitePieces['B'] < originalWhitePieces['B']) { whitePiecesTakenList.push('BB') }
            if (currentWhitePieces['N'] < originalWhitePieces['N']) { whitePiecesTakenList.push('BN') }

            whitePiecesTakenList.sort()
            blackPiecesTakenList.sort()
            for (let elements = 0; elements < whitePiecesTakenList.length; elements++) {
                temp.push(toUnicode(whitePiecesTakenList[elements]))
            }
            whitePiecesTakenList = temp
            temp = []
            for (let elements = 0; elements < blackPiecesTakenList.length; elements++) {
                temp.push(toUnicode(blackPiecesTakenList[elements]))
            }
            blackPiecesTakenList = temp
            whitePiecesTakenText = (whitePiecesTakenList.length > 0) ? whitePiecesTakenList.toString() : ' '
            blackPiecesTakenText = (blackPiecesTakenList.length > 0) ? blackPiecesTakenList.toString() : ' '

            if (LastMovesList === undefined) { LastMovesList = [] }
            LastMovesList.push(toUnicode(currentPiece.toLocaleUpperCase()) + ' > ' + currentMove[1])
            if (LastMovesList.length > 3) { LastMovesList.shift() }
            LastMovesList.reverse()
            LastMovesText = (LastMovesList.length > 0) ? LastMovesList.toString() : ' '
            LastMovesList.reverse()

            changewhite_pieces_taken_text(whitePiecesTakenText)
            changeblack_pieces_taken_text(blackPiecesTakenText)
            changelast_moves_text(LastMovesText)

            LastMovesText = ',' + LastMovesText

            turn = (turn === 'W') ? 'B' : 'W';
            console.log(turn)
            previosMoves.push(currentMove);
            currentMove = [];
            buttonpressed = true
            moveDone = false

            console.log(previosMoves)

            checkmate = isCheckmate(currentLayout, turn, previosMoves)
            console.log(checkmate)
            if (checkmate === true) {
                console.log('checkamte')
            }
        }
    };

    function onDrop(fromSquare, toSquare, piece) {
        let MoveSuccesfulTuple = [];
        fromSquare = String(fromSquare).toUpperCase();
        toSquare = String(toSquare).toUpperCase();
        previosMove = currentMove
        currentMove = [fromSquare, toSquare]
        if (currentLayout[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]][0] === turn) {
            if (buttonpressed === false) {
                let inverseMove = [previosMove[1], previosMove[0]]     //must depend on the button being pressed
                if (currentLayout[toTuple(inverseMove[0])[1]][toTuple(inverseMove[0])[0]][0] === turn && fromSquare === inverseMove[0] && toSquare === inverseMove[1]) {
                    currentPiece = piece
                    moveDone = move()
                    currentMove = []
                    moveDone = false
                    LastMovesText = '--' + LastMovesText
                    changelast_moves_text(LastMovesText)
                    LastMovesText = LastMovesText.slice(2, LastMovesText.length)
                    buttonpressed = true
                    return true
                } else {
                    currentMove = inverseMove
                    moveDone = move()
                    LastMovesText = '--' + LastMovesText
                    changelast_moves_text(LastMovesText)
                    LastMovesText = LastMovesText.slice(2, LastMovesText.length)
                    fromSquare = previosMove[0]
                    currentMove = []
                    moveDone = false
                }
            };
            if (moveDone === false) {
                MoveSuccesfulTuple = MoveSuccessful(fromSquare, toSquare, currentLayout, turn, previosMoves);
                if (MoveSuccesfulTuple[0] === true) {
                    currentPiece = piece
                    currentMove = MoveSuccesfulTuple[1]
                    moveDone = move()
                    if (LastMovesText.length < 1) { LastMovesText = '---' }
                    changelast_moves_text(LastMovesText)
                    LastMovesText = LastMovesText.slice(1, LastMovesText.length)
                    buttonpressed = false
                    return true
                } else {
                    currentMove = []
                    moveDone = false
                    return false;
                }
            };
        }
    }

    function move() {
        let boardCopy = currentLayout
        let fromSquare = currentMove[0]
        let toSquare = currentMove[1]
        if (currentMove.length === 3) {
            if (currentMove[2][0][1] === 'Q' || currentMove[2][0][1] === 'B' || currentMove[2][0][1] === 'R' || currentMove[2][0][1] === 'N') {
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = currentMove[2][0]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
            } else {
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
                boardCopy[toTuple(currentMove[2][0])[1]][toTuple(currentMove[2][0])[0]] = 'MT'
            }
        } else if (boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]][1]==='K') {
            if (fromSquare==='E8'&&toSquare==='G8') {
                boardCopy[toTuple('F8')[1]][toTuple('F8')[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]][0]+'R'
                boardCopy[toTuple('H8')[1]][toTuple('H8')[0]] = 'MT'
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
            } else if (fromSquare==='E8'&&toSquare==='C8') {
                boardCopy[toTuple('D8')[1]][toTuple('D8')[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]][0]+'R'
                boardCopy[toTuple('A8')[1]][toTuple('A8')[0]] = 'MT'
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
            } else if (fromSquare==='E1'&&toSquare==='G1') {
                boardCopy[toTuple('F1')[1]][toTuple('F1')[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]][0]+'R'
                boardCopy[toTuple('H1')[1]][toTuple('H1')[0]] = 'MT'
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
            } else if (fromSquare==='E1'&&toSquare==='C1') {
                boardCopy[toTuple('D1')[1]][toTuple('D1')[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]][0]+'R'
                boardCopy[toTuple('A1')[1]][toTuple('A1')[0]] = 'MT'
                boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
                boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
            }
        } else {
            boardCopy[toTuple(toSquare)[1]][toTuple(toSquare)[0]] = boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]]
            boardCopy[toTuple(fromSquare)[1]][toTuple(fromSquare)[0]] = 'MT'
        };
        currentLayout = boardCopy
        currentString = toDict(currentLayout)
        upadteCurrentString()
        return true
    }

    return (
        <div className="ChessFrontEnd">
            <h1>Peasant's Revolt Chess</h1>
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
                            boxShadow: '0 5px 15px rgb(0, 0, 0, 0.5)'
                        }}
                        customDarkSquareStyle={{ backgroundColor: '#1f1f1f' }}
                        customLightSquareStyle={{ backgroundColor: '#d6d6d6' }}
                        customDropSquareStyle={{ boxShadow: 'inset 0 0 1px 6px rgba(255,255,255,0.75)' }}
                        customPremoveDarkSquareStyle={{ backgroundColor: '#470a61' }}
                        customPremoveLightSquareStyle={{ backgroundColor: '#6c4080' }}
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
                        <h2 className='black_pieces_taken_header'>Pieces Taken By User</h2>
                        <Text style={styles.black_pieces_taken_text} className='black_pieces_taken_text' id='black_pieces_taken_text'>{black_pieces_taken_text}</Text>
                    </span>

                    <span className='white_pieces_taken'>
                        <h2 className='white_pieces_taken_header'>Pieces Taken By AI</h2>
                        <Text style={styles.white_pieces_taken_text} className='white_pieces_taken_text' id='white_pieces_taken_text'>{white_pieces_taken_text}</Text>
                    </span>
                    <span className='disclaimer'>
                        <p className='disclaimer_text'>Data about the chess games, such as what moves were made and in what order, are stored so that the AI can learn and get better at chess. No data about the user is stored.</p>
                    </span>
                </div>
            </div>
        </div>
    );
};

export { OnePlayerPeasantsRevoltChess };