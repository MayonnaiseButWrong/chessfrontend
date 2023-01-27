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

    function generateQMoves() {
        var moves=[];
        var direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(i),Number(0)]);};
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(-i),Number(0)]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(0),Number(i)]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(0),Number(-i)]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(i),Number(i)]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(i),Number(-i)]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(-i),Number(i)]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([Number(-i),Number(-i)]);}
        moves.push(direction);
        return moves
    }

    function generateBMoves() {
        var moves=[];
        var direction=[];
        for (let i = 0; i < 10; i++) {direction.push([i,i]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([-i,i]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([-i,-i]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([i,-i]);}
        moves.push(direction);
        return moves
    };

    function generateRMoves() {
        var moves=[];
        var direction=[];
        for (let i = 0; i < 10; i++) {direction.push([i,0]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([-i,0]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([0,i]);}
        moves.push(direction);
        direction=[];
        for (let i = 0; i < 10; i++) {direction.push([0,-i]);}
        moves.push(direction);
        return moves
    }

    function toCoOrdinates(InputTuple) {
        const letters=['A','B','C','D','E','F','G','H']
        return letters[(InputTuple[0])]+String(8-InputTuple[1])
    }

    function toTuple(InputCoOrdinates) {
        const letters=['A','B','C','D','E','F','G','H']
        return [Number(letters.findIndex(InputCoOrdinates[0])),8-Number(InputCoOrdinates[1])]
    }

    function checkPawnSpecialMove(currentLayout,turn,previosMovesList) {
        var moves=[];
        var currentPiece='';
        if (turn==='B') {
            for (let i = 0; i < 8; i++) {
                if ((currentLayout[6][i])==='BP') {
                    if (currentLayout[5][i]==='MT') {
                        if (currentLayout[6][i][0]==='W'||currentLayout[6][i]==='MT') {
                            moves.push([toCoOrdinates([i,1]),toCoOrdinates([i,3 ])]);
                        };
                    };
                };
            };
        };
        if (turn==='W') {
            for (let i = 0; i < 8; i++) {
                if ((currentLayout[6][i])==='WP') {
                    if (currentLayout[5][i]==='MT') {
                        if (currentLayout[6][i][0]==='B'||currentLayout[6][i]==='MT') {
                            moves.push([toCoOrdinates([i,6]),toCoOrdinates([i,4])]);
                        };
                    };
                };
            };
        };

        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                currentPiece=currentLayout[j][i]
                if (currentPiece[1]==='P') {
                    if (turn==='W'&&turn===currentPiece[0]) {
                        if (i===0||currentLayout[j-1][1][0]==='B') {
                            moves.push([toCoOrdinates([0,j]),toCoOrdinates([1,j-1])]);
                        } else if (i===7||currentLayout[j-1][6][0]==='B') {
                            moves.push([toCoOrdinates([7,j]),toCoOrdinates([6,j-1])]);
                        };
                    };
                    if (turn==='B'&&turn===currentPiece[0]) {
                        if (i===0||currentLayout[j+1][1][0]==='B') {
                            moves.push([toCoOrdinates([0,j]),toCoOrdinates([1,j+1])]);
                        } else if (i===7||currentLayout[j+1][6][0]==='B') {
                            moves.push([toCoOrdinates([7,j]),toCoOrdinates([6,j+1])]);
                        };
                    };
                };
            };
        };
        //add en passant here
        return moves
    };

    function checkVectors (currentLayout,turn) {
        var Qmoves=generateQMoves();
        var Bmoves=generateBMoves();
        var Rmoves=generateRMoves();
        const moveVectors = {
            'Q': Qmoves,
            'K': [[[1,0]],[[1,1]],[[0,1]],[[-1,1]],[[-1,0]],[[-1,-1]],[[0,-1]],[[0,-1]]],
            'B': Bmoves,
            'N': [[[2,1]],[[1,2]],[[-1,2]],[[-2,1]],[[-2,-1]],[[-1,-2]],[[1,-2]],[[2,-1]]],
            'R': Rmoves,
            'P': [[[0,1]]]
        }
        var moves=[];
        var vector=[];
        var currenDirection=[];
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                if (!(currentLayout[j][i]==='MT')){
                    for (let direction = 0; direction < moveVectors[currentLayout[j][i][1]].length; direction++) {
                        currenDirection= moveVectors[currentLayout[j][i][1]][direction]
                        for (let vectorNumber = 0; vectorNumber <currenDirection.length; vectorNumber++) {
                            vector=moveVectors[currentLayout[j][i][1]][direction][vectorNumber]
                            if (turn==='B') {
                                if (currentLayout[j][i][0]==='B') {
                                    if ((j+vector[1])<8&&(j+vector[1])>=0&&(i+vector[0])<8&&(i+vector[0])>=0){
                                        if (currentLayout[j+vector[1]][i+vector[0]]==='MT'||currentLayout[j+vector[1]][i+vector[0]][0]==='W') {
                                            moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j+vector[1]])]);
                                        } else {
                                            vectorNumber=currenDirection.length;
                                            break;
                                        };
                                    };
                                };
                            };
                            if (turn==='W') {
                                if (currentLayout[j][i][0]==='W') {
                                    if ((j-vector[1])<8&&(j-vector[1])>=0&&(i+vector[0])<8&&(i+vector[0])>=0) {
                                        if (currentLayout[j-vector[1]][i+vector[0]]==='MT' ||currentLayout[j-vector[1]][i+vector[0]][0]==='B') {
                                            moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j-vector[1]])]);
                                        } else {
                                            vectorNumber=currenDirection.length;
                                            break;
                                        };
                                    };
                                };
                            };
                        };
                    };
                };
            };
        };
        return moves
    };

    function castling (previosMovesList,turn) {
        var flag = false;
        const letters=['A','B','C','D','E','F','G','H']
        if (turn==='W'){
            if (previosMovesList.includes([toTuple('E1'),toTuple('E2')])||previosMovesList.includes([toTuple('E1'),toTuple('F1')])||previosMovesList.includes([toTuple('E1'),toTuple('F2')])||previosMovesList.includes([toTuple('E1'),toTuple('D1')])||previosMovesList.includes([toTuple('E1'),toTuple('D2')])) {
                return []
            };
            for (let i = 1; i < 9; i++) {
                if (previosMovesList.includes([toTuple('A1'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('A1'),toTuple(letters[i-1]+'1')])) {
                    flag=true
                };
                if (previosMovesList.includes([toTuple('H1'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('H1'),toTuple(letters[i-1]+'1')])) {
                    flag=true
                };
            };
            if (flag===false){
                return [['E1','C1'],['E1','G1']]
            };
        };
        if (turn==='B'){
            if (previosMovesList.includes([toTuple('E8'),toTuple('E7')])||previosMovesList.includes([toTuple('E8'),toTuple('F8')])||previosMovesList.includes([toTuple('E8'),toTuple('F7')])||previosMovesList.includes([toTuple('E8'),toTuple('D8')])||previosMovesList.includes([toTuple('E8'),toTuple('D7')])) {
                return []
            };
            for (let i = 1; i < 9; i++) {
                if (previosMovesList.includes([toTuple('A8'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('A8'),toTuple(letters[i-1]+'8')])) {
                    flag=true
                };
                if (previosMovesList.includes([toTuple('H8'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('H8'),toTuple(letters[i-1]+'8')])) {
                    flag=true
                };
            };
            if (flag===false){
                return [['E8','C8'],['E8','G8']]
            };
        };
    };

    function castlingIsPossibe(currentLayout,turn) {
        if (turn === 'B' ) {
            for (let i = 0; i < 8; i++) {
                if (!(currentLayout[0][i]==='MT')) {
                    return false
                };
            };
        };
        if (turn === 'W' ) {
            for (let i = 0; i < 8; i++) {
                if (!(currentLayout[7][i]==='MT')) {
                    return false
                };
            };
        };
        return true
    };

    ////setTimeout() => {
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

    function generatePossibleMoves(currentLayout,turn,previosMovesList) {
        var moves=[];
        var PawnSpecialMoves=[];
        //check if there is a check
        moves=checkVectors(currentLayout,turn)
        PawnSpecialMoves=checkPawnSpecialMove(currentLayout,turn,previosMovesList)
        moves=moves.concat(PawnSpecialMoves);
        if (castlingIsPossibe(currentLayout,turn)===true) {
            moves.concat(castling(previosMovesList,turn));
        }
        return moves
    }
    
    var moves = []
    moves=generatePossibleMoves(currentLayout,'W',[]);
    console.log(moves.toString());

    function OnClick (square){
        console.log('here2');
    };

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