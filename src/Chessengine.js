import { toTuple, toCoOrdinates } from './translations.js'

var AllMoves = [];

//https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/
//https://acloudguru.com/blog/engineering/create-a-serverless-python-api-with-aws-amplify-and-flask

function clone(ins) { //clones a board layout using the ability to turn an array into a string. This is necessary to create seperate objects in memory when assigning a new object, rather than the default behavior to create a new pointer to the same object in memory.
    let string = ins.toString()
    let word = ''
    let letter = ''
    let out = []
    let temp = []
    for (let i = 0; i < string.length; i++) {
        letter = string[i]
        if (letter === ',') {
            temp.push(word)
            word = ''
            if (temp.length >= 8) {
                out.push(temp)
                temp = []
            }
        } else {
            word += letter
        }
    }
    temp.push(word)
    out.push(temp)
    return out
}

function generateQMoves() {
    let moves = [];
    let direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(i), Number(0)]); };
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(-i), Number(0)]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(0), Number(i)]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(0), Number(-i)]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(i), Number(i)]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(i), Number(-i)]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(-i), Number(i)]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([Number(-i), Number(-i)]); }
    moves.push(direction);
    return moves
}

function generateBMoves() {
    let moves = [];
    let direction = [];
    for (let i = 1; i < 10; i++) { direction.push([i, i]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([-i, i]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([-i, -i]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([i, -i]); }
    moves.push(direction);
    return moves
};

function generateRMoves() {
    let moves = [];
    let direction = [];
    for (let i = 1; i < 10; i++) { direction.push([i, 0]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([-i, 0]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([0, i]); }
    moves.push(direction);
    direction = [];
    for (let i = 1; i < 10; i++) { direction.push([0, -i]); }
    moves.push(direction);
    return moves
}

function findKing(currentLayout, turn) {
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            if (turn === 'W') {
                if (currentLayout[j][i] === 'WK') {
                    return toCoOrdinates([i, j])
                }
            }
            if (turn === 'B') {
                if (currentLayout[j][i] === 'BK') {
                    return toCoOrdinates([i, j])
                }
            }
        };
    };
};

function checkPawnSpecialMove(currentLayout, turn, previosMovesList) {
    let moves = [];
    let pawnNormalMoves = [];
    let enPassantMoves = [];
    if (turn === 'B') {
        for (let i = 0; i < 8; i++) {
            if ((currentLayout[1][i]) === 'BP') {
                if (currentLayout[2][i] === 'MT') {
                    if (currentLayout[3][i] === 'MT') {
                        moves.push([toCoOrdinates([i, 1]), toCoOrdinates([i, 3])]);
                    };
                };
            };
        };
    };
    if (turn === 'W') {
        for (let i = 0; i < 8; i++) {
            if ((currentLayout[6][i]) === 'WP') {
                if (currentLayout[5][i] === 'MT') {
                    if (currentLayout[4][i] === 'MT') {
                        moves.push([toCoOrdinates([i, 6]), toCoOrdinates([i, 4])]);
                    };
                };
            };
        };
    };

    enPassantMoves = enPassant(currentLayout, turn, previosMovesList)
    moves = moves.concat(enPassantMoves)
    pawnNormalMoves = pawnNormal(currentLayout, turn, false)
    moves = moves.concat(pawnNormalMoves)
    return moves
};

function pawnNormal(currentLayout, turn, isOpponentMoves) {
    let moves = []
    let currentPiece = ''
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            currentPiece = currentLayout[j][i]
            if (currentPiece[1] === 'P') {
                if (turn === 'W' && turn === currentPiece[0]) {
                    if (i < 7 && currentLayout[j - 1][i + 1][0] === 'B') {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + 1, j - 1])]);
                    };
                    if (i > 0 && currentLayout[j - 1][i - 1][0] === 'B') {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i - 1, j - 1])]);
                    };
                    if (currentLayout[j - 1][i] === 'MT') {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i, j - 1])]);
                    }
                    if (isOpponentMoves === true) {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + 1, j - 1])]);
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i - 1, j - 1])]);
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i, j - 1])]);
                    }
                }
                if (turn === 'B' && turn === currentPiece[0]) {
                    if (i < 7 && currentLayout[j + 1][i + 1][0] === 'W') {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + 1, j + 1])]);
                    };
                    if (i > 0 && currentLayout[j + 1][i - 1][0] === 'W') {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i - 1, j + 1])]);
                    };
                    if (currentLayout[j + 1][i] === 'MT') {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i, j + 1])]);
                    }
                    if (isOpponentMoves === true) {
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + 1, j + 1])]);
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i - 1, j + 1])]);
                        moves.push([toCoOrdinates([i, j]), toCoOrdinates([i, j + 1])]);
                    }
                };
            };
        };
    };
    return moves
}

function enPassant(currentLayout, turn, previosMovesList) {
    let positionList = [];
    let enPassantMoves = [];
    let startSquare = '';
    let endSquare = '';
    let includes = false;
    for (let i = 0; i < 8; i++) {
        if (turn === 'W') {
            if (currentLayout[3][i] === 'WP') {
                if (i < 7 && currentLayout[3][i + 1] === 'BP') {
                    startSquare = toCoOrdinates([i, 3]);
                    endSquare = toCoOrdinates([i + 1, 2])
                    for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === toCoOrdinates([i + 1, 1]) && previosMovesList[a][1] === toCoOrdinates([i + 1, 3])) { includes = true } }
                    if (includes = true) {
                        positionList = []
                        positionList.push(toCoOrdinates([i + 1, 3]));
                        enPassantMoves.push([startSquare, endSquare, positionList])
                    }
                };
                if (i > 0 && currentLayout[3][i - 1] === 'BP') {
                    startSquare = toCoOrdinates([i, 3]);
                    endSquare = toCoOrdinates([i - 1, 2]);
                    for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === toCoOrdinates([i - 1, 1]) && previosMovesList[a][1] === toCoOrdinates([i - 1, 3])) { includes = true } }
                    if (includes === true) {
                        positionList = []
                        positionList.push(toCoOrdinates([i - 1, 3]));
                        enPassantMoves.push([startSquare, endSquare, positionList])
                    }
                };
            };
        };
        if (turn === 'B') {
            if (currentLayout[4][i] === 'BP') {
                if (i < 7 && currentLayout[4][i + 1] === 'WP') {
                    startSquare = toCoOrdinates([i, 4]);
                    endSquare = toCoOrdinates([i + 1, 5]);
                    for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === toCoOrdinates([i + 1, 6]) && previosMovesList[a][1] === toCoOrdinates([i + 1, 4])) { includes = true } }
                    if (includes === true) {
                        positionList = []
                        positionList.push(toCoOrdinates([i + 1, 4]));
                        enPassantMoves.push([startSquare, endSquare, positionList])
                    }
                };
                if (i > 0 && currentLayout[4][i - 1] === 'WP') {
                    startSquare = toCoOrdinates([i, 4]);
                    endSquare = toCoOrdinates([i - 1, 5]);
                    for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === toCoOrdinates([i - 1, 6]) && previosMovesList[a][1] === toCoOrdinates([i - 1, 4])) { includes = true } }
                    if (includes === true) {
                        positionList = []
                        positionList.push(toCoOrdinates([i - 1, 4]));
                        enPassantMoves.push([startSquare, endSquare, positionList])
                    }
                };
            };
        };
    };
    return enPassantMoves
};

function opponentKingMoves(KingPosition) {
    let moves = []
    let i = 0
    let j = 0
    KingPosition = toTuple(KingPosition)
    i = KingPosition[0]
    j = KingPosition[1]
    const vectors = [[[1, 0]], [[1, 1]], [[0, 1]], [[-1, 1]], [[-1, 0]], [[-1, -1]], [[0, -1]], [[1, -1]]]
    for (let vector = 0; vector < vector.length; vector++) {
        if ((vectors[vector][0][0] + i) >= 0 && (vectors[vector][0][0] + i) < 8 && (vectors[vector][0][1] + j) >= 0 && (vectors[vector][0][1] + j) < 8) {
            moves.push([toCoOrdinates([i, j]), toCoOrdinates([vectors[vector][0][0] + i, vectors[vector][0][1] + j])])
        }
    }
    return moves
}

function isCheckAfterMoveingKing(kingposition, layout) {
    let modifier = (layout[kingposition[1]][kingposition[0]][0] === 'W') ? 'B' : 'W'
    let m = (modifier === 'B') ? 1 : -1
    if (kingposition[0] - 1 >= 0 && kingposition[1] + m * 1 < 8 && kingposition[1] + m * 1 >= 0 && layout[kingposition[1] + m * 1][kingposition[0] - 1] === 'WP') { return true }
    if (kingposition[0] + 1 < 8 && kingposition[1] + m * 1 < 8 && kingposition[1] + m * 1 >= 0 && layout[kingposition[1] + m * 1][kingposition[0] + 1] === 'WP') { return true }
    let vectors = [[[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]], [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0]], [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],], [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9],], [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9],], [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9],], [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9],], [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]], [[2, 1]], [[1, 2]], [[-2, 1]], [[-1, 2]], [[2, -1]], [[1, -2]], [[-1, -2]], [[-2, -1]]]
    let direction = []
    let vector = []
    for (let a = 0; a < vectors.length; a++) {
        direction = vectors[a]
        for (let b = 0; b < direction.length; b++) {
            vector = direction[b]
            if (vector[1] + kingposition[1] < 8 && vector[1] + kingposition[1] >= 0 && vector[0] + kingposition[0] < 8 && vector[0] + kingposition[0] >= 0) {
                if ((vector[0] === 1 || vector[1] === 1) && layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]] === modifier + 'K') { return true }
                if (Math.abs(vector[0]) === Math.abs(vector[1]) && (layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]] === modifier + 'Q' || layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]] === modifier + 'B')) { return true }
                else if ((vector[0] === 0 || vector[1] === 0) && (layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]] === modifier + 'Q' || layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]] === modifier + 'R')) { return true }
                else if (layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]] === modifier + 'N') { return true }
                if (layout[vector[1] + kingposition[1]][vector[0] + kingposition[0]][0] === layout[kingposition[1]][kingposition[0]][0]) { break }
            }
        }
    }
    return false
}

function kingMoves(KingPosition, opponentMoves, boardLayout) {
    let moves = []
    let i = 0
    let j = 0
    let flag = false
    let vector = []
    let move = []
    let piece = []
    let boardcopy = []
    KingPosition = toTuple(KingPosition)
    i = KingPosition[0]
    j = KingPosition[1]
    const vectors = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    for (let a = 0; a < vectors.length; a++) {
        vector = vectors[a]
        flag = false
        for (let b = 0; b < opponentMoves.legnth; b++) {
            move = opponentMoves[b]
            piece = toTuple(move[1])
            if (((i + vector[0]) === piece[0]) && ((j + vector[1]) === piece[1])) { flag = true }
        }
        if ((i + vector[0]) < 8 && (i + vector[0]) >= 0 && (j + vector[1]) < 8 && (j + vector[1]) >= 0) {
            if (boardLayout[j + vector[1]][i + vector[0]][0] === boardLayout[j][i][0] && boardLayout[j + vector[1]][i + vector[0]] !== 'MT') { flag = true }
        }
        if ((i + vector[0]) < 8 && (i + vector[0]) >= 0 && (j + vector[1]) < 8 && (j + vector[1]) >= 0) {
            boardcopy = clone(boardLayout)
            boardcopy[j + vector[1]][i + vector[0]] = boardcopy[j][i]
            boardcopy[j][i] = 'MT'
            let temp = isCheckAfterMoveingKing([i + vector[0], j + vector[1]], boardcopy)
            if (flag === false && boardLayout[j + vector[1]][i + vector[0]][0] !== boardLayout[j][i][0] && temp === false) { moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j + vector[1]])]) }
        }
    }
    return moves
}

function checkVectors(currentLayout, turn, KingPosition, isOpponentMoves) {
    let Qmoves = generateQMoves();
    let Bmoves = generateBMoves();
    let Rmoves = generateRMoves();
    let kingI = 0
    let kingJ = 0
    KingPosition = toTuple(KingPosition)
    kingI = KingPosition[0]
    kingJ = KingPosition[1]
    const moveVectors = {
        'Q': Qmoves,
        'K': [[[1, 0]], [[1, 1]], [[0, 1]], [[-1, 1]], [[-1, 0]], [[-1, -1]], [[0, -1]], [[0, -1]]],
        'B': Bmoves,
        'N': [[[2, 1]], [[1, 2]], [[-1, 2]], [[-2, 1]], [[-2, -1]], [[-1, -2]], [[1, -2]], [[2, -1]]],
        'R': Rmoves,
    }
    let moves = [];
    let vector = [];
    let currenDirection = [];
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            if (!(currentLayout[j][i] === 'MT')) {
                if (!(currentLayout[j][i][1] === 'K' || currentLayout[j][i][1] === 'P')) {
                    if (turn === 'B') {
                        if (currentLayout[j][i][0] === 'B') {
                            for (let direction = 0; direction < moveVectors[currentLayout[j][i][1]].length; direction++) {
                                currenDirection = moveVectors[currentLayout[j][i][1]][direction]
                                for (let vectorNumber = 0; vectorNumber < currenDirection.length; vectorNumber++) {
                                    vector = moveVectors[currentLayout[j][i][1]][direction][vectorNumber]
                                    if (isCheckUsingVector(kingI, kingJ, i, j, currentLayout, [i + vector[0], j + vector[1]]) === false) {
                                        if ((j + vector[1]) < 8 && (j + vector[1]) >= 0 && (i + vector[0]) < 8 && (i + vector[0]) >= 0) {
                                            if (currentLayout[j + vector[1]][i + vector[0]][0] === 'W') {
                                                moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j + vector[1]])]);
                                                break;
                                            } else if (currentLayout[j + vector[1]][i + vector[0]] === 'MT') {
                                                moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j + vector[1]])]);
                                            } else {
                                                if (isOpponentMoves === true) {
                                                    moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j + vector[1]])]);
                                                }
                                                break;
                                            };
                                        };
                                    }
                                };
                            };
                        };
                    };
                    if (turn === 'W') {
                        if (currentLayout[j][i][0] === 'W') {
                            for (let direction = 0; direction < moveVectors[currentLayout[j][i][1]].length; direction++) {
                                currenDirection = moveVectors[currentLayout[j][i][1]][direction]
                                for (let vectorNumber = 0; vectorNumber < currenDirection.length; vectorNumber++) {
                                    vector = moveVectors[currentLayout[j][i][1]][direction][vectorNumber]
                                    if (isCheckUsingVector(kingI, kingJ, i, j, currentLayout, [i + vector[0], j - vector[1]]) === false) {
                                        if ((j - vector[1]) < 8 && (j - vector[1]) >= 0 && (i + vector[0]) < 8 && (i + vector[0]) >= 0) {
                                            if (currentLayout[j - vector[1]][i + vector[0]][0] === 'B') {
                                                moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j - vector[1]])]);
                                                break;
                                            } else if (currentLayout[j - vector[1]][i + vector[0]] === 'MT') {
                                                moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j - vector[1]])]);
                                            } else {
                                                if (isOpponentMoves === true) {
                                                    moves.push([toCoOrdinates([i, j]), toCoOrdinates([i + vector[0], j - vector[1]])]);
                                                }
                                                break;
                                            };
                                        };
                                    }
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

function castling(previosMovesList, turn, currentLayout) {
    let l = true;
    let r = true;
    let currentSquare = [];
    let Line = [];
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    let includes = false
    if (turn === 'W') {
        for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === 'E1' && (previosMovesList[a][1] === 'E2' || previosMovesList[a][1] === 'F1' || previosMovesList[a][1] === 'F2' || previosMovesList[a][1] === 'D1' || previosMovesList[a][1] === 'D2')) { includes = true } }
        if (includes === true) {
            return []
        };
        for (let i = 1; i < 9; i++) {
            includes = false
            for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === 'A1' && (previosMovesList[a][1] === 'A' + String(i) || previosMovesList[a][1] === letters[i - 1] + '1')) { includes = true } }
            if (includes === true) {
                return []
            };
            includes = false
            for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === 'H1' && (previosMovesList[a][1] === 'H' + String(i) || previosMovesList[a][1] === letters[i - 1] + '1')) { includes = true } }
            if (includes === true) {
                return []
            };
        };
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                currentSquare = currentLayout[j][i];
                if (!(currentSquare === 'MT' || currentSquare[1] === 'K') && currentSquare[0] === 'B') {
                    for (let position = 0; position < 8; position++) {
                        Line = findLine(toCoOrdinates([i, j]), currentSquare[1], toCoOrdinates([position, 7]));
                        if (Line.length > 0) {
                            for (let positionOnLine = 0; positionOnLine < Line.length; positionOnLine++) {
                                if (!(currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0] === 'B')) {
                                    if (currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]] === 'MT') {
                                        if (!(currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0] === 'WK')) {
                                            if (toTuple(Line[positionOnLine])[1] === 7) {
                                                if (toTuple(Line[positionOnLine])[0] < 5) {
                                                    l = false
                                                } else if (toTuple(Line[positionOnLine])[0] > 5) {
                                                    r = false
                                                } else {
                                                    return []
                                                }
                                            }
                                        };
                                    } else {
                                        break
                                    }
                                } else {
                                    break
                                };
                            };
                        };
                        Line = []
                    };
                };
            };
        };
        if (!(currentLayout[7][1] === 'MT') || !(currentLayout[7][2] === 'MT') || !(currentLayout[7][3] === 'MT')) { l = false }
        if (!(currentLayout[7][5] === 'MT') || !(currentLayout[7][6] === 'MT')) { r = false }
        if (l === true && r === true) {
            return [['E1', 'C1'], ['E1', 'G1']]
        } else if (l === false && r === false) {
            return []
        } else if (l === false) {
            return [['E1', 'G1']]
        } else if (r === false) {
            return [['E1', 'C1']]
        };
    };
    if (turn === 'B') {
        for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === 'E8' && (previosMovesList[a][1] === 'E7' || previosMovesList[a][1] === 'F8' || previosMovesList[a][1] === 'F7' || previosMovesList[a][1] === 'D8' || previosMovesList[a][1] === 'D7')) { includes = true } }
        if (includes === true) {
            return []
        };
        for (let i = 1; i < 9; i++) {
            includes = false
            for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === 'A8' && (previosMovesList[a][1] === 'A' + String(i) || previosMovesList[a][1] === letters[i - 1] + '8')) { includes = true } }
            if (includes === true) {
                return []
            };
            includes = false
            for (let a = 0; a < previosMovesList.length; a++) { if (previosMovesList[a][0] === 'H8' && (previosMovesList[a][1] === 'H' + String(i) || previosMovesList[a][1] === letters[i - 1] + '8')) { includes = true } }
            if (includes === true) {
                return []
            };
        };
        for (let j = 0; j < 8; j++) {
            for (let i = 0; i < 8; i++) {
                currentSquare = currentLayout[j][i];
                if (!(currentSquare === 'MT' || currentSquare[1] === 'K') && currentSquare[0] === 'W') {
                    for (let position = 0; position < 8; position++) {
                        Line = findLine(toCoOrdinates([i, j]), currentSquare[1], toCoOrdinates([position, 0]));
                        if (Line.length > 0) {
                            for (let positionOnLine = 0; positionOnLine < Line.length; positionOnLine++) {
                                if (!(currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0] === 'W')) {
                                    if (currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]] === 'MT') {
                                        if (!(currentLayout[toTuple(Line[positionOnLine])[1]][toTuple(Line[positionOnLine])[0]][0] === 'BK')) {
                                            if (toTuple(Line[positionOnLine])[1] === 0) {
                                                if (toTuple(Line[positionOnLine])[0] < 5) {
                                                    l = false
                                                } else if (toTuple(Line[positionOnLine])[0] > 5) {
                                                    r = false
                                                } else {
                                                    return []
                                                }
                                            }
                                        };
                                    } else {
                                        break
                                    }
                                } else {
                                    break
                                };;
                            };
                        };
                        Line = []
                    };
                };
            };
        };
        if (!(currentLayout[0][1] === 'MT') || !(currentLayout[0][2] === 'MT') || !(currentLayout[0][3] === 'MT')) { l = false }
        if (!(currentLayout[0][5] === 'MT') || !(currentLayout[0][6] === 'MT')) { r = false }
        if (l === true && r === true) {
            return [['E8', 'C8'], ['E8', 'G8']]
        } else if (l === false && r === false) {
            return []
        } else if (l === false) {
            return [['E8', 'G8']]
        } else if (r === false) {
            return [['E8', 'C8']]
        };
    };
    return []
};

function isCheckUsingVector(kingI, kingJ, pieceI, pieceJ, boardLayout, endSquare) {
    let vector = [pieceI - kingI, pieceJ - kingJ]
    let modulus = 0
    let unitVector = []
    let flag = false
    if (vector[0] === vector[1] || vector[0] === -vector[1] || vector[0] === 0 || vector[1] === 0) {
        if (vector[0] < 0) {
            modulus = -vector[0]
        } else if (vector[0] > 0) {
            modulus = vector[0]
        } else if (vector[1] < 0) {
            modulus = -vector[1]
        } else {
            modulus = vector[1]
        }
        unitVector = [vector[0] / modulus, vector[1] / modulus]
        for (let mod = 1; mod < 10; mod++) {
            if (kingI + mod * unitVector[0] >= 0 && kingJ + mod * unitVector[1] >= 0 && kingI + mod * unitVector[0] < 8 && kingJ + mod * unitVector[1] < 8) {
                if (kingI + mod * unitVector[0] === endSquare[0] && kingJ + mod * unitVector[1] === endSquare[1]) { return false }
                if ([kingI + mod * unitVector[0], kingI + mod * unitVector[1]] === [pieceI, pieceJ]) { flag = true }
                if (flag === true) {
                    if (!((boardLayout[kingJ + mod * unitVector[1]][kingI + mod * unitVector[0]][0] === boardLayout[kingJ][kingI][0]) && (boardLayout[kingJ + mod * unitVector[1]][kingI + mod * unitVector[0]][1] === 'P' || boardLayout[kingJ + mod * unitVector[1]][kingI + mod * unitVector[0]][1] === 'K' || boardLayout[kingJ + mod * unitVector[1]][kingI + mod * unitVector[0]] === 'MT'))) {
                        return true
                    }
                } else {
                    if (boardLayout[kingJ + mod * unitVector[1]][kingI + mod * unitVector[0]][0] === boardLayout[kingJ][kingI][0]) {
                        return false
                    }
                }
            }
        }
    }
    return false
}

function findLine(position1, piece, position2) {
    let vector = [];
    let Qmoves = generateQMoves();
    let Bmoves = generateBMoves();
    let Rmoves = generateRMoves();
    let Line = [];
    let modulus = 0
    let unitVector = []
    let mod = 1
    let currentVector = []
    let vectors = {
        'Q': Qmoves,
        'B': Bmoves,
        'R': Rmoves,
    }
    piece = String(piece)
    if (piece === 'N' || piece === 'P') {
        return [position1]
    }
    vector = [toTuple(position2)[0] - toTuple(position1)[0], toTuple(position2)[1] - toTuple(position1)[1]]
    if (vector[0] === vector[1] || vector[0] === -vector[1] || vector[0] === 0 || vector[1] === 0) {
        if (vector[0] < 0) {
            modulus = -vector[0]
        } else if (vector[0] > 0) {
            modulus = vector[0]
        } else if (vector[1] < 0) {
            modulus = -vector[1]
        } else {
            modulus = vector[1]
        }
        unitVector = [vector[0] / modulus, vector[1] / modulus]
        for (let direction = 0; direction < vectors[piece].length; direction++) {
            for (let directionVector = 0; directionVector < vectors[piece][direction].length; directionVector++) {
                if (toCoOrdinates(vectors[piece][direction][directionVector]) === toCoOrdinates(unitVector)) {
                    currentVector = [toTuple(position1)[0] + mod * unitVector[0], toTuple(position1)[1] + mod * unitVector[1]]
                    while (!(toCoOrdinates(currentVector) === position2) && mod < 10) {
                        Line.push(toCoOrdinates(currentVector))
                        mod++
                        currentVector = [toTuple(position1)[0] + mod * unitVector[0], toTuple(position1)[1] + mod * unitVector[1]]
                    }
                    Line.push(toCoOrdinates(currentVector))
                }
            }
        }
    }
    return Line
};

function isCheck(boardLayout, KingPosition, opponentMoves) {
    let i = toTuple(KingPosition)[0]
    let j = toTuple(KingPosition)[1]
    if (opponentMoves.length === 0) { return [] }
    let VectorsOfPieces = {
        'Q': [[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]], [[0, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0]], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],], [[0, 0], [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9],], [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9],], [[0, 0], [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9],], [[0, 0], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9],], [[0, 0], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]],
        'K': [[[0, 0], [1, 0]], [[0, 0], [-1, 0]], [[0, 0], [0, 1]], [[0, 0], [-0, 1]], [[0, 0], [1, 1]], [[0, 0], [-1, 1]], [[0, 0], [1, -1]], [[0, 0], [-1, -1]]],
        'B': [[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]], [[0, 0], [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9]], [[0, 0], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9]], [[0, 0], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9],]],
        'R': [[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]], [[0, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0]], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],], [[0, 0], [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9],]],
        'N': [[[0, 0], [2, 1]], [[0, 0], [1, 2]], [[0, 0], [-2, 1]], [[0, 0], [-1, 2]], [[0, 0], [2, -1]], [[0, 0], [1, -2]], [[0, 0], [-1, -2]], [[0, 0], [-2, -1]]],
        'P': [[[0, 0], [1, 1]], [[0, 0], [-1, 1]]]
    }
    let squares = []
    let flag = false
    let move = []
    let includes = false
    let direction = []
    let vector = []
    let vectors = []
    let modifier = (boardLayout[toTuple(opponentMoves[0][0])[1]][toTuple(opponentMoves[0][0])[0]][0] == 'B') ? 1 : -1
    for (let a = 0; a < opponentMoves.length; a++) {
        move = (opponentMoves[a].length === 2) ? [toTuple(opponentMoves[a][0]), toTuple(opponentMoves[a][1])] : [toTuple(opponentMoves[a][0]), toTuple(opponentMoves[a][1]), opponentMoves[a][2]]
        if (move[1][0] === i && move[1][1] === j) {
            vectors=VectorsOfPieces[boardLayout[move[0][1]][move[0][0]][1]]
            for (let b = 0; b < vectors.length; b++) {
                direction = vectors[b]
                for (let c = 0; c < direction.length; c++) {
                    vector = direction[c]
                    includes = false
                    if (move[0][0] + modifier * vector[0] < 8 && move[0][0] + modifier * vector[0] >= 0 && move[0][1] + modifier * vector[1] < 8 && move[0][1] + modifier * vector[1] >= 0) {
                        for (let d = 0; d < direction.length; d++) { if (opponentMoves[d][0] === toCoOrdinates(move[0]) && opponentMoves[d][1] === toCoOrdinates([move[0][0] + modifier * vector[0], move[0][1] + modifier * vector[1]])) { includes = true } }
                        if (includes === true) {
                            flag = true
                        } else if (flag === true) {
                            squares.push(toCoOrdinates([move[0][0] + modifier * vector[0], move[0][1] + modifier * vector[1]]))
                        }
                    }
                }
            }
        }
    }
    return squares

}

function generateOpponenMoves(currentLayout, turn) {
    turn = (turn === 'W') ? 'B' : 'W'
    let opponentMoves = [];
    let PawnMoves = [];
    let kMoves = []
    let KingPosition = []
    KingPosition = findKing(currentLayout, turn)
    opponentMoves = checkVectors(currentLayout, turn, KingPosition, true)
    PawnMoves = pawnNormal(currentLayout, turn, true)
    opponentMoves = opponentMoves.concat(PawnMoves);
    kMoves = opponentKingMoves(KingPosition)
    opponentMoves = opponentMoves.concat(kMoves)
    return opponentMoves
}

function generatePossibleMoves(currentLayout, turn, previosMovesList, castlingPossible) {
    castlingPossible = true
    let moves = [];
    let PawnSpecialMoves = [];
    let check = {};
    let KingPosition = '';
    let checkMoves = [];
    let opponentMoves = [];
    let kMoves = []
    let castlingMoves = []
    let move = []
    let includes = false
    let count = 0
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            if (!(currentLayout[j][i] === 'MT')) {
                count+=1
            }
        }
    }
    if (count <=2) {return [[],false] }
    opponentMoves = generateOpponenMoves(currentLayout, turn)
    KingPosition = findKing(currentLayout, turn);
    moves = checkVectors(currentLayout, turn, KingPosition, false);
    PawnSpecialMoves = checkPawnSpecialMove(currentLayout, turn, previosMovesList);
    moves = moves.concat(PawnSpecialMoves);
    kMoves = kingMoves(KingPosition, opponentMoves, currentLayout)
    moves = moves.concat(kMoves)
    check = isCheck(currentLayout, KingPosition, opponentMoves);
    if (castlingPossible === true) {
        castlingMoves = castling(previosMovesList, turn, currentLayout)
    }
    moves = moves.concat(castlingMoves);
    if (check.length<=0) {
        for (let Move = 0; Move < moves.length; Move++) {
            if (moves === undefined) { moves.splice(Move, 1) }
        }
        return [moves, false]
    } else {
        for (let a = 0; a < moves.length; a++) {
            move = (moves[a].length === 2) ? [toTuple(moves[a][0]), toTuple(moves[a][1])] : [toTuple(moves[a][0]), toTuple(moves[a][1]), moves[a][2]]
            includes = false
            let boardcopy = clone(currentLayout)
            boardcopy[move[1][1]][move[1][0]] = boardcopy[move[0][1]][move[0][0]]
            boardcopy[move[0][1]][move[0][0]] = 'MT'
            for (let b = 0; b < moves.length; b++) { if (toTuple(move[1])===check[b]) {includes = true}}
            if (currentLayout[move[0][1]][move[0][0]][1]==='K') {
                if (!(includes === true) && isCheckAfterMoveingKing([move[1][1], move[1][0]], boardcopy)==false) {checkMoves.push(moves[a])}
            } else {
                if (includes === true && isCheckAfterMoveingKing([move[1][1], move[1][0]], boardcopy)==false) {checkMoves.push(moves[a])}
            }
        }
        return [checkMoves, true]
    };
};

function MoveSuccessful(fromSquare, toSquare, currentLayout, turn, previosMoves, castlingPossible) {
    let buffer = generateMoves(currentLayout, turn, previosMoves, castlingPossible);
    let moves = buffer[0]
    for (let Move = 0; Move < moves.length; Move++) {
        if (moves[Move][0] === fromSquare && moves[Move][1] === toSquare) {
            return [true, moves[Move]];
        };
    };
    return [false, ['nope']];
};

function isCheckmate(currentLayout, turn, previosMoves, castlingPossible) {
    let buffer = generateMoves(currentLayout, turn, previosMoves, castlingPossible);
    let moves = buffer[0]
    let isCheck = buffer[1]
    if (moves.length < 1) {
        if (isCheck === true) {
            return true
        } else {
            return 'Stalemate'
        }
    }
    return false
}

function generateMoves(currentLayout, turn, previosMoves) {
    AllMoves = generatePossibleMoves(currentLayout, turn, previosMoves);
    return AllMoves
}



export { MoveSuccessful, isCheckmate };
