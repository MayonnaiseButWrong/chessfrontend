import {toTuple,toCoOrdinates} from './translations.js'

var generatedBefore = false;
var AllMoves = [];

//fix king moves
//fix pawn moves

function generateQMoves() {
    let moves=[];
    let direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(i),Number(0)]);};
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(-i),Number(0)]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(0),Number(i)]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(0),Number(-i)]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(i),Number(i)]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(i),Number(-i)]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(-i),Number(i)]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([Number(-i),Number(-i)]);}
    moves.push(direction);
    return moves
}

function generateBMoves() {
    let moves=[];
    let direction=[];
    for (let i = 1; i < 10; i++) {direction.push([i,i]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([-i,i]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([-i,-i]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([i,-i]);}
    moves.push(direction);
    return moves
};

function generateRMoves() {
    let moves=[];
    let direction=[];
    for (let i = 1; i < 10; i++) {direction.push([i,0]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([-i,0]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([0,i]);}
    moves.push(direction);
    direction=[];
    for (let i = 1; i < 10; i++) {direction.push([0,-i]);}
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
            if (turn==='B'){
                if (currentLayout[j][i]==='BK') {
                    return toCoOrdinates([i,j])
                }
            }
        };
    };
};

function checkPawnSpecialMove(currentLayout,turn,previosMovesList) {
    let moves=[];
    let currentPiece='';
    let enPassantMoves=[];
    let promotionMoves=[];
    if (turn==='B') {
        for (let i = 0; i < 8; i++) {
            if ((currentLayout[1][i])==='BP') {
                if (currentLayout[2][i]==='MT') {
                    if (currentLayout[3][i][0]==='W'||currentLayout[3][i]==='MT') {
                        moves.push([toCoOrdinates([i,1]),toCoOrdinates([i,3])]);
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
                    if (i<7&&currentLayout[j-1][i+1][0]==='B') {
                        moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+1,j-1])]);
                    };
                    if (i>0&&currentLayout[j-1][i-1][0]==='B') {
                            moves.push([toCoOrdinates([i,j]),toCoOrdinates([i-1,j-1])]);
                    };
                    if (currentLayout[j-1][i]==='MT') {
                        moves.push([toCoOrdinates([i,j]),toCoOrdinates([i,j-1])]);
                    }
                }
                if (turn==='B'&&turn===currentPiece[0]) {
                    if (i<7&&currentLayout[j+1][i+1][0]==='W') {
                        moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+1,j+1])]);
                    };
                    if (i>0&&currentLayout[j+1][i-1][0]==='W') {
                            moves.push([toCoOrdinates([i,j]),toCoOrdinates([i-1,j+1])]);
                    };
                    if (currentLayout[j+1][i]==='MT') {
                        moves.push([toCoOrdinates([i,j]),toCoOrdinates([i,j+1])]);
                    }
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
    let j = 0;
    let flag =false;
    let positionList=[];
    let temp=0;
    let enPassantMoves=[];
    let startSquare='';
    let endSquare='';
    let templist=[];
    for (let i = 0; i < 8; i++) {
        if (turn==='W') {
            if (currentLayout[3][i]==='WP') {
                if (i<7&&currentLayout[3][i+1]==='BP') {
                    temp=i;
                    j=3;
                    startSquare=toCoOrdinates([i,j]);
                    i++;
                    while (i<7&&j>1&&flag===false) {
                        flag=true;
                        if (currentLayout[j][i]==='BP') {
                            flag=false;
                            positionList.push(toCoOrdinates([i,j]));
                        };
                        j--;
                        i++;
                    };
                    i-=2
                    j+=1
                    endSquare=toCoOrdinates([i,j]);
                    i=temp;
                    if (j===1){
                        templist.push('WQ')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('WB')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('WN')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('WR')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                    } else {enPassantMoves.push([startSquare,endSquare,positionList]);};
                };
                if (i>0&&currentLayout[3][i-1]==='BP') {
                    temp=i;
                    j=3;
                    startSquare=toCoOrdinates([i,j]);
                    i--;
                    while (i>=0&&j>1&&flag===false) {
                        flag=true;
                        if (i<6&&currentLayout[j][i]==='BP') {
                            flag=false;
                            positionList.push(toCoOrdinates([i,j]));
                        };
                        j--;
                        i--;
                    };
                    i+=2
                    j+=1
                    endSquare=toCoOrdinates([i,j]);
                    i=temp;
                    if (j===1){
                        templist.push('WQ')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('WB')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('WN')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('WR')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                    } else {enPassantMoves.push([startSquare,endSquare,positionList]);};
                };
            };
        };
        if (turn==='B') {
            if (currentLayout[4][i]==='BP') {
                if (i<7&&currentLayout[4][i+1]==='WP') {
                    temp=i;
                    j=4;
                    startSquare=toCoOrdinates([i,j]);
                    i++;
                    while (i<7&&j<6&&flag===false) {
                        flag=true;
                        if (currentLayout[j][i]==='WP') {
                            flag=false;
                            positionList.push(toCoOrdinates([i,j]));
                        };
                        j++;
                        i++;
                    };
                    i-=2
                    j-=1
                    endSquare=toCoOrdinates([i,j]);
                    i=temp;
                    if (j===6){
                        templist.push('BQ')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('BB')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('BN')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('BR')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                    } else {enPassantMoves.push([startSquare,endSquare,positionList]);};
                };
                if (i>0&&currentLayout[4][i-1]==='WP') {
                    temp=i;
                    j=4;
                    startSquare=toCoOrdinates([i,j]);
                    i--;
                    while (i>0&&j<6&&flag===false) {
                        flag=true;
                        if (currentLayout[j][i]==='WP') {
                            flag=false;
                            positionList.push(toCoOrdinates([i,j]));
                        };
                        j++;
                        i--;
                    };
                    i+=2
                    j-=1
                    endSquare=toCoOrdinates([i,j]);
                    i=temp;
                    if (j===6){
                        templist.push('BQ')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('BB')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('BN')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                        templist=[]
                        templist.push('BR')
                        templist=templist.concat(positionList)
                        enPassantMoves.push([startSquare,endSquare,templist])
                    } else {enPassantMoves.push([startSquare,endSquare,positionList]);};
                };//penis
            };
        };
    };
    return enPassantMoves
};

function Promotion(currentLayout,turn) {
    let promotionMoves = [];
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

function opponentKingMoves (KingPosition) {
    let moves=[]
    let i=0
    let j=0
    KingPosition=toTuple(KingPosition)
    i=KingPosition[0]
    j=KingPosition[1]
    const vectors=[[[1,0]],[[1,1]],[[0,1]],[[-1,1]],[[-1,0]],[[-1,-1]],[[0,-1]],[[0,-1]]]
    for (let vector = 0; vector < 8; vector++) {
        if ((vectors[vector][0]+i)>=0 && (vectors[vector][0]+i)<8 && (vectors[vector][1]+j)>=0 && (vectors[vector][1]+j)<8) {
            moves.push([vectors[vector][0]+i,vectors[vector][1]+j])
        }
    }
    return moves
}

function kingMoves (KingPosition,opponentMoves) {
    let moves=[]
    let i=0
    let j=0
    KingPosition=toTuple(KingPosition)
    i=KingPosition[0]
    j=KingPosition[1]
    const vectors=[[[1,0]],[[1,1]],[[0,1]],[[-1,1]],[[-1,0]],[[-1,-1]],[[0,-1]],[[0,-1]]]
    for (let vector = 0; vector < 8; vector++) {
        if ((vectors[vector][0]+i)>=0 && (vectors[vector][0]+i)<8 && (vectors[vector][1]+j)>=0 && (vectors[vector][1]+j)<8) {
            for (let move = 0; move < 8; move++) {
                if ((opponentMoves[move][1]===[vectors[vector][0]+i,vectors[vector][1]+j])){
                    moves.push([vectors[vector][0]+i,vectors[vector][1]+j])
                }
            }
        }
    }
    return moves
}

function checkVectors (currentLayout,turn,KingPosition) {
    let Qmoves=generateQMoves();
    let Bmoves=generateBMoves();
    let Rmoves=generateRMoves();
    let kingI=0
    let kingJ=0
    KingPosition=toTuple(KingPosition)
    kingI=KingPosition[0]
    kingJ=KingPosition[1]
    const moveVectors = {
        'Q': Qmoves,
        'K': [[[1,0]],[[1,1]],[[0,1]],[[-1,1]],[[-1,0]],[[-1,-1]],[[0,-1]],[[0,-1]]],
        'B': Bmoves,
        'N': [[[2,1]],[[1,2]],[[-1,2]],[[-2,1]],[[-2,-1]],[[-1,-2]],[[1,-2]],[[2,-1]]],
        'R': Rmoves,
    }
    let moves=[];
    let vector=[];
    let currenDirection=[];
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            if (!(currentLayout[j][i]==='MT')){
                if (!(currentLayout[j][i][1]==='K'||currentLayout[j][i][1]==='P')) {
                    if (turn==='B') {
                        if (currentLayout[j][i][0]==='B') {
                            if (isCheckUsingVector(kingI,kingJ,i,j,currentLayout)===false) {
                                console.log('here 17')
                                for (let direction = 0; direction < moveVectors[currentLayout[j][i][1]].length; direction++) {
                                    currenDirection= moveVectors[currentLayout[j][i][1]][direction]
                                    for (let vectorNumber = 0; vectorNumber <currenDirection.length; vectorNumber++) {
                                        vector=moveVectors[currentLayout[j][i][1]][direction][vectorNumber]
                                        if ((j+vector[1])<8&&(j+vector[1])>=0&&(i+vector[0])<8&&(i+vector[0])>=0){
                                            if (currentLayout[j+vector[1]][i+vector[0]][0]==='W') {
                                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j+vector[1]])]);
                                                break;
                                            } else if (currentLayout[j+vector[1]][i+vector[0]]==='MT') {
                                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j+vector[1]])]);
                                            } else {
                                                break;
                                            };
                                        };
                                    };
                                };
                            };
                        };
                    };
                    if (turn==='W') {
                        if (currentLayout[j][i][0]==='W') {
                            if (isCheckUsingVector(kingI,kingJ,i,j,currentLayout)===false) {
                                for (let direction = 0; direction < moveVectors[currentLayout[j][i][1]].length; direction++) {
                                    currenDirection= moveVectors[currentLayout[j][i][1]][direction]
                                    for (let vectorNumber = 0; vectorNumber <currenDirection.length; vectorNumber++) {
                                        vector=moveVectors[currentLayout[j][i][1]][direction][vectorNumber]
                                        if ((j-vector[1])<8&&(j-vector[1])>=0&&(i+vector[0])<8&&(i+vector[0])>=0) {
                                            if (currentLayout[j-vector[1]][i+vector[0]][0]==='B') {
                                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j-vector[1]])]);
                                                break;
                                            } else if (currentLayout[j-vector[1]][i+vector[0]]==='MT') {
                                                moves.push([toCoOrdinates([i,j]),toCoOrdinates([i+vector[0],j-vector[1]])]);
                                            } else {
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
        };
    };
    return moves
};

function castling (previosMovesList,turn,opponentMoves,currentLayout) {
    let l=true;
    let r=true;
    let currentSquare=[];
    let Line=[];
    const letters=['A','B','C','D','E','F','G','H']
    if (turn==='W'){
        if (previosMovesList.includes([toTuple('E1'),toTuple('E2')])||previosMovesList.includes([toTuple('E1'),toTuple('F1')])||previosMovesList.includes([toTuple('E1'),toTuple('F2')])||previosMovesList.includes([toTuple('E1'),toTuple('D1')])||previosMovesList.includes([toTuple('E1'),toTuple('D2')])) {
            return []
        };
        for (let i = 1; i < 9; i++) {
            if (previosMovesList.includes([toTuple('A1'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('A1'),toTuple(letters[i-1]+'1')])) {
                return []
            };
            if (previosMovesList.includes([toTuple('H1'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('H1'),toTuple(letters[i-1]+'1')])) {
                return []
            };
        };
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                currentSquare=currentLayout[j][i];
                if(!(currentSquare==='MT')&&currentSquare[0]==='B'){
                    for (let position = 0; position < 8; position++) {
                        Line=findLine(toCoOrdinates([i,j]),currentSquare[1],toCoOrdinates([position,7]));
                        if (Line.length>0) {
                            for (let positionOnLine = 0; positionOnLine < Line.length; positionOnLine++) {
                                if (currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0]==='W'&&!(currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0]==='WK')) {
                                    if (Line[positionOnLine][1]<5) {
                                        l=false
                                    } else if (Line[positionOnLine][1]>5) {
                                        r=false
                                    } else {
                                        return []
                                    }
                                };
                            };
                        };
                    };
                };
            };
        };
        if (l===false&&r===false) {
            return [['E1','C1'],['E1','G1']]
        } else if (l===false) {
            return [['E1','G1']]
        } else if (r===false) {
            return [['E1','C1']]
        };
    };
    if (turn==='B'){
        if (previosMovesList.includes([toTuple('E8'),toTuple('E7')])||previosMovesList.includes([toTuple('E8'),toTuple('F8')])||previosMovesList.includes([toTuple('E8'),toTuple('F7')])||previosMovesList.includes([toTuple('E8'),toTuple('D8')])||previosMovesList.includes([toTuple('E8'),toTuple('D7')])) {
            return []
        };
        for (let i = 1; i < 9; i++) {
            if (previosMovesList.includes([toTuple('A8'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('A8'),toTuple(letters[i-1]+'8')])) {
                return []
            };
            if (previosMovesList.includes([toTuple('H8'),toTuple('A'+String(i))])||previosMovesList.includes([toTuple('H8'),toTuple(letters[i-1]+'8')])) {
                return []
            };
        };
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                currentSquare=currentLayout[j][i];
                if(!(currentSquare==='MT')&&currentSquare[0]==='W'){
                    for (let position = 0; position < 8; position++) {
                        Line=findLine(toCoOrdinates([i,j]),currentSquare[1],toCoOrdinates([position,0]));
                        if (Line.length>0) {
                            for (let positionOnLine = 0; positionOnLine < Line.length; positionOnLine++) {
                                if (currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0]==='B'&&!(currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0]==='BK')) {
                                    if (Line[positionOnLine][1]<5) {
                                        l=false
                                    } else if (Line[positionOnLine][1]>5) {
                                        r=false
                                    } else {
                                        return []
                                    }
                                };
                            };
                        };
                    };
                };
            };
        };
        if (l===false&&r===false) {
            return [['E1','C1'],['E1','G1']]
        } else if (l===false) {
            return [['E1','G1']]
        } else if (r===false) {
            return [['E1','C1']]
        };
    };
};

function isCheckUsingVector (kingI,kingJ,pieceI,pieceJ,boardLayout) {
    let vector=[pieceI-kingI,pieceJ-kingJ]
    let modulus=0
    let unitVector=[]
    if (vector[0]===vector[1]||vector[0]===-vector[1]||vector[0]===0||vector[1]===0){
        if (vector[0]<0) {
            modulus=-vector[0]
        } else if (vector[0]>0) {
            modulus=vector[0]
        } else if (vector[1]<0) {
            modulus=-vector[1]
        } else {
            modulus=vector[1]
        }
        unitVector=[vector[0]/modulus,vector[1]/modulus]
    
        for (let mod = 1;mod < 10; mod++){
            if (kingI+mod*unitVector[0]>=0&&kingJ+mod*unitVector[1]>=0&&kingI+mod*unitVector[0]<8&&kingJ+mod*unitVector[1]<8) {
                if (!(boardLayout[kingJ+mod*unitVector[1]][kingI+mod*unitVector[0]][0]===boardLayout[kingJ][kingI][0])) {
                    if (!(boardLayout[kingJ+mod*unitVector[1]][kingI+mod*unitVector[0]][1]==='P'||boardLayout[kingJ+mod*unitVector[1]][kingI+mod*unitVector[0]][1]==='K'||boardLayout[kingJ+mod*unitVector[1]][kingI+mod*unitVector[0]]==='MT')) {
                        return true
                    }
                }
            }
        }
    }
    return false
}

function castlingIsPossibe(currentLayout,turn) {
    if (turn === 'B' ) {
        for (let i = 0; i < 8; i++) {
            if (!(currentLayout[0][i]==='MT'||currentLayout[0][i]==='BR'||currentLayout[0][i]==='BK')) {
                return false
            };
        };
    };
    if (turn === 'W' ) {
        for (let i = 0; i < 8; i++) {
            if (!(currentLayout[7][i]==='MT'||currentLayout[7][i]==='WR'||currentLayout[7][i]==='WK')) {
                return false
            };
        };
    };
    return true
};

function findLine(position1,piece,position2){
    let Qmoves=generateQMoves();
    let Bmoves=generateBMoves();
    let Rmoves=generateRMoves();
    let vectors=[];
    let currentDirection=[];
    let vector =[];
    let Line=[];
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
    let position='';
    for (let Move = 0; Move < opponentMoves.length; Move++) {
        position=opponentMoves[Move][1]
        if (position===KingPosition) {
            return {'is Check':true,'position':position,'piece':currentLayout[toTuple(position)[1]][toTuple(position)[0]][1]}
        }
    };
    return {'is Check':false,'position':'somewhere','piece':'someone'}
}

function generateOpponenMoves(currentLayout,turn,previosMovesList) {
    turn=(turn==='W')?'B':'W'
    let opponentMoves=[];
    let opponentMovesWithoutCastling=[];
    let PawnSpecialMoves=[];
    let kMoves=[]
    let KingPosition=[]
    KingPosition=findKing(currentLayout,turn)
    console.log(KingPosition)
    opponentMoves=checkVectors(currentLayout,turn,KingPosition)
    PawnSpecialMoves=checkPawnSpecialMove(currentLayout,turn,previosMovesList)
    opponentMoves=opponentMoves.concat(PawnSpecialMoves);
    kMoves=opponentKingMoves(KingPosition)
    opponentMoves=opponentMoves.concat(kMoves)
    opponentMovesWithoutCastling=opponentMoves
    if (castlingIsPossibe(currentLayout,turn)===true) {
        opponentMoves.concat(castling(previosMovesList,turn,currentLayout));
    };
    for (let Move = 0; Move < opponentMoves.length; Move++) {
        if (opponentMoves===undefined) {opponentMoves.splice(Move,1)}
    }
    for (let Move = 0; Move < opponentMovesWithoutCastling.length; Move++) {
        if (opponentMovesWithoutCastling===undefined) {opponentMovesWithoutCastling.splice(Move,1)}
    }
    opponentMoves.pop()//remove these pls
    opponentMovesWithoutCastling.pop()
    return [opponentMoves,opponentMovesWithoutCastling]
}

function generatePossibleMoves(currentLayout,turn,previosMovesList) {
    let moves=[];
    let PawnSpecialMoves=[];
    let check={};
    let KingPosition='';
    let Line=[];
    let CheckMoves=[];
    let position='';
    let opponentMovesTuple=[];
    let opponentMoves=[];
    let opponentMovesWithoutCastling=[];
    let kMoves=[]
    opponentMovesTuple=generateOpponenMoves(currentLayout,turn,previosMovesList)
    opponentMoves=opponentMovesTuple[0]
    opponentMovesWithoutCastling=opponentMovesTuple[1]
    KingPosition=findKing(currentLayout,turn);
    moves=checkVectors(currentLayout,turn,KingPosition);
    console.log('here 17',moves.toLocaleString())
    PawnSpecialMoves=checkPawnSpecialMove(currentLayout,turn,previosMovesList);
    moves=moves.concat(PawnSpecialMoves);
    kMoves=kingMoves(KingPosition[0],KingPosition[1],opponentMoves)
    moves=moves.concat(kMoves)
    check=isCheck(currentLayout,KingPosition,opponentMoves);
    if (castlingIsPossibe(currentLayout,turn,moves,opponentMovesWithoutCastling)===true) {
        moves.concat(castling(previosMovesList,turn,currentLayout));
    };
    if (check['is Check']===false) {
        for (let Move = 0; Move < moves.length; Move++) {
            if (moves===undefined) {moves.splice(Move,1)}
        }
        return moves;
    } else {
        Line=findLine(KingPosition,check['piece'],check['position'])
        for (let Move = 0; Move < moves.length; Move++) {
            position=moves[Move][1]
            if (Line.includes(position)===true){
                CheckMoves.push(moves[Move])
            };
        };
        for (let Move = 0; Move < CheckMoves.length; Move++) {
            if (CheckMoves===undefined) {CheckMoves.splice(Move,1)}
        }
        return CheckMoves
    };
};

function MoveSuccessful (fromSquare, toSquare,currentLayout,turn,previosMoves) {
    let moves = generateMoves(currentLayout,turn,previosMoves);
    console.log('here2',fromSquare, toSquare);
    console.log(moves.toLocaleString());
    for (let Move = 0; Move < moves.length; Move++) {
        if (moves[Move][0]===fromSquare&&moves[Move][1]===toSquare) {
            console.log('ofevnj m')
            return [true,moves[Move]];
        };
    };
    return [false,['nope']];
};

function isCheckmate (currentLayout,turn,previosMoves) {
    generatedBefore=false
    let moves = generateMoves(currentLayout,turn,previosMoves);
    console.log(moves)
    if (moves.length<0) {
        return true
    }
    return false
}

function generateMoves(currentLayout,turn,previosMoves) {
        AllMoves = generatePossibleMoves(currentLayout,turn,previosMoves);
    return AllMoves
}

export {MoveSuccessful, isCheckmate};
