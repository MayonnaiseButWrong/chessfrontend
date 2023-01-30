import './Chess.css'
import {Link} from 'react-router-dom'
import { Chessboard } from "react-chessboard";
import { Chess } from 'chess.js';
import toFen from './listToFEN.js'

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

    function findKing(currentLayout,turn){
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                if (turn==='W'){
                    if (currentLayout[j][i]==='WK') {
                        return toCoOrdinates([i,j])
                    }
                }
                if (turn==='W'){
                    if (currentLayout[j][i]==='BK') {
                        return toCoOrdinates([i,j])
                    }
                }
            };
        };
    };

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
        var enPassantMoves=[];
        var promotionMoves=[];
        if (turn==='B') {
            for (let i = 0; i < 8; i++) {
                if ((currentLayout[1][i])==='BP') {
                    if (currentLayout[2][i]==='MT') {
                        if (currentLayout[3][i][0]==='W'||currentLayout[3][i]==='MT') {
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
                        if (currentLayout[4][i][0]==='B'||currentLayout[4][i]==='MT') {
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
                        if (i<7&&currentLayout[j-1][i+1][0]==='B'){
                            moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+1,j-1])]);
                        };
                        if (i>0&&currentLayout[j-1][i-1][0]==='B')
                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i-1,j-1])]);
                        };
                    if (turn==='B'&&turn===currentPiece[0]) {
                        if (i<7&&currentLayout[j+1][i+1][0]==='B'){
                            moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+1,j+1])]);
                        };
                        if (i>0&&currentLayout[j+1][i-1][0]==='B')
                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i-1,j+1])]);
                    };
                };
            };
        };
        enPassantMoves=enPassant(currentLayout,turn,previosMovesList)
        promotionMoves=Promotion(currentLayout,turn)
        moves=moves.concat(enPassantMoves)
        moves=moves.concat(promotionMoves)
        return moves
    };

    function enPassant(currentLayout,turn,previosMovesList) {
        var j = 0;
        var flag =false;
        var positionList=[];
        var temp=0;
        var enPassantMoves=[];
        var startSquare='';
        var endSquare='';
        for (let i = 0; i < 8; j++) {
            if (turn==='W') {
                if (currentLayout[3][i]==='WP') {
                    if (i<6&&currentLayout[3][i+1]==='BP') {
                        temp=i;
                        j=3;
                        i++;
                        startSquare=toCoOrdinates([i,j]);
                        positionList.push(toCoOrdinates([i+1,j]));
                        while (i<8&&j>1&&flag===false) {
                            j--;
                            i++;
                            flag=true;
                            if (i<6&&currentLayout[j][i]==='BP') {
                                flag=false;
                                positionList.push(toCoOrdinates([i,j]));
                            };
                        };
                        endSquare=toCoOrdinates([i,j-1]);
                        i=temp;
                        enPassantMoves.push([startSquare,endSquare,positionList])
                    };
                    if (i<6&&currentLayout[3][i-1]==='BP') {
                        temp=i;
                        j=3;
                        i--;
                        startSquare=toCoOrdinates([i,j]);
                        positionList.push(toCoOrdinates([i+1,j]));
                        while (i<8&&j>1&&flag===false) {
                            j--;
                            i--;
                            flag=true;
                            if (i<6&&currentLayout[j][i]==='BP') {
                                flag=false;
                                positionList.push(toCoOrdinates([i,j]));
                            };
                        };
                        endSquare=toCoOrdinates([i,j-1]);
                        i=temp;
                        enPassantMoves.push([startSquare,endSquare,positionList])
                    };
                };
            };
            if (turn==='B') {
                if (currentLayout[4][i]==='BP') {
                    if (i<6&&currentLayout[4][i+1]==='WP') {
                        temp=i;
                        j=4;
                        i++;
                        startSquare=toCoOrdinates([i,j]);
                        positionList.push(toCoOrdinates([i+1,j]));
                        while (i<8&&j<6&&flag===false) {
                            j++;
                            i++;
                            flag=true;
                            if (i<6&&currentLayout[j][i]==='WP') {
                                flag=false;
                                positionList.push(toCoOrdinates([i,j]));
                            };
                        };
                        endSquare=toCoOrdinates([i,j+1]);
                        i=temp;
                        enPassantMoves.push([startSquare,endSquare,positionList])
                    };
                    if (i<6&&currentLayout[4][i-1]==='WP') {
                        temp=i;
                        j=4;
                        i--;
                        startSquare=toCoOrdinates([i,j]);
                        positionList.push(toCoOrdinates([i+1,j]));
                        while (i<8&&j<6&&flag===false) {
                            j++;
                            i--;
                            flag=true;
                            if (i<6&&currentLayout[j][i]==='WP') {
                                flag=false;
                                positionList.push(toCoOrdinates([i,j]));
                            };
                        };
                        endSquare=toCoOrdinates([i,j+1]);
                        i=temp;
                        enPassantMoves.push([startSquare,endSquare,positionList])
                    };//penis
                };
            };
        };
    };

    function Promotion(currentLayout,turn) {
        var promotionMoves = [];
        for (let i = 0; i < 8; i++) {
            if (turn==='W') {
                if (currentLayout[1][i]==='WP') {
                    promotionMoves.push([toCoOrdinates([i,1]),toCoOrdinates([i,0]),['WQ']])
                    promotionMoves.push([toCoOrdinates([i,1]),toCoOrdinates([i,0]),['WB']])
                    promotionMoves.push([toCoOrdinates([i,1]),toCoOrdinates([i,0]),['WR']])
                    promotionMoves.push([toCoOrdinates([i,1]),toCoOrdinates([i,0]),['WK']])
                };
            };
            if (turn==='B'){
                if (currentLayout[6][i]==='BP') {
                    promotionMoves.push([toCoOrdinates([i,6]),toCoOrdinates([i,7]),['BQ']])
                    promotionMoves.push([toCoOrdinates([i,6]),toCoOrdinates([i,7]),['BB']])
                    promotionMoves.push([toCoOrdinates([i,6]),toCoOrdinates([i,7]),['BR']])
                    promotionMoves.push([toCoOrdinates([i,6]),toCoOrdinates([i,7]),['BK']])
                };
            };
        };
        return promotionMoves
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
                                            if (!(currentLayout[j][i][1]==='P'&&i===6)) {
                                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j+vector[1]])]);
                                            };
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
                                            if (!(currentLayout[j][i][1]==='P'&&i===1)) {
                                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j-vector[1]])]);
                                            }
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

    function castling (previosMovesList,turn,opponentMoves) {
        var flag = false;
        var l=true;
        var r=true;
        var position=''
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
                for (let Move = 0; Move < opponentMoves.length; Move++) {
                    position=opponentMoves[Move][1]
                    if (position[1]===String(1)) {
                        if (position[1]<5) {
                            l=true
                        } else {
                            r=true
                        };
                        flag=true
                    };
                };
            };
            if (flag===false||(l===false&&r===false)) {
                return [['E1','C1'],['E1','G1']]
            };
            if (l===false) {
                return [['E1','G1']]
            }
            if (r===false) {
                return [['E1','C1']]
            }
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
                for (let Move = 0; Move < opponentMoves.length; Move++) {
                    position=opponentMoves[Move][1]
                    if (position[1]===String(8)) {
                        if (position[1]<5) {
                            l=true
                        } else {
                            r=true
                        };
                        flag=true
                    };
                };
            };
            if (flag===false){
                return [['E8','C8'],['E8','G8']]
            };
            if (l===false) {
                return [['E8','G8']]
            }
            if (r===false) {
                return [['E8','C8']]
            }
        };
    };

    function castlingIsPossibe(currentLayout,turn,opponentMoves) {
        if (turn === 'B' ) {
            for (let i = 0; i < 8; i++) {
                if (!(currentLayout[0][i]==='MT'||currentLayout[0][i]==='BR'||currentLayout[0][i]==='BK')) {
                    return false
                };
                if (opponentMoves.includes([i,0])) {
                    return false
                };
            };
        };
        //not finished
        return true
    };

    function findLine(position1,piece,position2){
        var Qmoves=generateQMoves();
        var Bmoves=generateBMoves();
        var Rmoves=generateRMoves();
        var vectors=[];
        var currentDirection=[];
        var vector =[];
        var Line=[];
        const moveVectors = {
            'Q': Qmoves,
            'K': [[[1,0]],[[1,1]],[[0,1]],[[-1,1]],[[-1,0]],[[-1,-1]],[[0,-1]],[[0,-1]]],
            'B': Bmoves,
            'N': [[[2,1]],[[1,2]],[[-1,2]],[[-2,1]],[[-2,-1]],[[-1,-2]],[[1,-2]],[[2,-1]]],
            'R': Rmoves,
            'P': [[[0,1]]]
        }
        vectors=moveVectors[piece]
        for (let direction = 0; direction < vectors.length; direction++) {
            currentDirection= vectors[direction]
            for (let vectorNumber = 0; vectorNumber <currentDirection.length; vectorNumber++) {
                vector=currentDirection[vectorNumber]
                if ((toTuple(position1)[0]+vector[0])===(toTuple(position2)[0])&&(toTuple(position1)[1]+vector[1])===(toTuple(position2)[1])) {
                    for (let x = 0; x<vectorNumber; x++ ) {
                        vector=currentDirection[vectorNumber]
                        Line.push(toCoOrdinates([(toTuple(position1)[0]+vector[0]),(toTuple(position1)[1]+vector[1])]))
                    };
                    return Line
                };
            };
        };
    };

    function isCheck(currentLayout,KingPosition,opponentMoves) {
        var position='';
        for (let Move = 0; Move < opponentMoves.length; Move++) {
            position=opponentMoves[Move][1]
            if (position===KingPosition) {
                return {'is Check':true,'position':position,'piece':currentLayout[toTuple(position)[1]][toTuple(position)[0]][1]}
            }
        };
        return {'is Check':false,'position':'somewhere','piece':'someone'}
    }

    function generateOpponenMovesWithoutCastling(currentLayout,turn,previosMovesList) {
        turn=(turn==='W')?'B':'W'
        var opponentMoves=[];
        var opponentMovesWithoutCastling=[];
        var PawnSpecialMoves=[];
        opponentMoves=checkVectors(currentLayout,turn)
        PawnSpecialMoves=checkPawnSpecialMove(currentLayout,turn,previosMovesList)
        opponentMoves=opponentMoves.concat(PawnSpecialMoves);
        opponentMovesWithoutCastling=opponentMoves
        if (castlingIsPossibe(currentLayout,turn)===true) {
            opponentMoves.concat(castling(previosMovesList,turn));
        };
        return [opponentMoves,opponentMovesWithoutCastling]
    }

    //setTimeout(startingString=setString(),10000);
//
    function setString () {
    startingString = toFen([
        ['BR','BN','BB','BQ','BK','BB','BN','BR'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','WP','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['WP','WP','WP','WP','MT','WP','WP','WP'],
        ['WR','WN','WB','WQ','WK','WB','WN','WR']
        ])
        console.log(startingString)
        return startingString
    }
    console.log(startingString)
    
    var currentLayout=[
        ['BR','BN','BB','BQ','BK','BB','BN','BR'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['WP','WP','WP','WP','WP','WP','WP','WP'],
        ['WR','WN','WB','WQ','WK','WB','WN','WR']
        ];

    function generatePossibleMoves(currentLayout,turn,previosMovesList) {
        var moves=[];
        var PawnSpecialMoves=[];
        var check={};
        var KingPosition='';
        var Line=[];
        var CheckMoves=[];
        var position='';
        var opponentMovesTuple=[];
        var opponentMoves=[];
        var opponentMovesWithoutCastling=[];
        opponentMovesTuple=generateOpponenMovesWithoutCastling(currentLayout,turn,previosMovesList)
        opponentMoves=opponentMovesTuple[0]
        opponentMovesWithoutCastling=opponentMovesTuple[1]
        KingPosition=findKing(currentLayout,turn);
        moves=checkVectors(currentLayout,turn);
        PawnSpecialMoves=checkPawnSpecialMove(currentLayout,turn,previosMovesList);
        moves=moves.concat(PawnSpecialMoves);
        check=isCheck(currentLayout,KingPosition,opponentMoves);
        if (castlingIsPossibe(currentLayout,turn,moves,opponentMovesWithoutCastling)===true) {
            moves.concat(castling(previosMovesList,turn));
        };
        if (check['is Check']===false) {
            return moves;
        } else {
            Line=findLine(KingPosition,check['piece'],check['position'])
            for (let Move = 0; Move < moves.length; Move++) {
                position=moves[Move][1]
                if (Line.includes(position)===true){
                    CheckMoves.push(moves[Move])
                };
            };
            return CheckMoves
        };
    };
    
    //var moves = []
    //moves=generatePossibleMoves(currentLayout,'W',[]);
    //console.log(moves.toString());

    function MoveSuccessful (sourceSquare, targetSquare, piece) {
        var sourceSquare = sourceSquare.toUpperCase();
        var targetSquare = targetSquare.toUpperCase();
        var piece = piece.toUpperCase();
        var moves = generatePossibleMoves(currentLayout,'W',[]);
        console.log('here2',sourceSquare, targetSquare, piece);
        console.log(moves.toLocaleString());
        for (let Move = 0; Move < moves.length; Move++) {
            if (moves[Move][0]===sourceSquare&&moves[Move][1]===targetSquare) {
                console.log('ofevnj m')
                return true;
            };
        };
        return false;
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
