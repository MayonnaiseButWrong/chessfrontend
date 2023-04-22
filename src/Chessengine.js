import { toFEN } from './translations.js'
import { Chess } from 'chess.js'

function MoveSuccessful(fromSquare, toSquare, startingLayout, previosMoves, castlingPossible) {
    let game = (castlingPossible==true)? new Chess(toFEN(startingLayout)+' w KQkq - 0 1'):new Chess(toFEN(startingLayout)+' w - - 0 1')
    let p = previosMoves.map((x) => x)
    for (let i = 0; i < p.length; i++) {game.move({from:p[i][0].toLowerCase(),to:p[i][1].toLowerCase()})}
    let moves = game.moves({verbose:true})
    for (let a = 0; a < moves.length; a++) {if (moves[a]['from'].toUpperCase()===fromSquare && moves[a]['to'].toUpperCase()===toSquare) {return [true, [fromSquare,toSquare]]}}
    return [false,['nope']]
}

function isCheckmate(startingLayout, previosMoves, castlingPossible) {
    let game = (castlingPossible==true)? new Chess(toFEN(startingLayout)+' w KQkq - 0 1'):new Chess(toFEN(startingLayout)+' w - - 0 1')
    let p = previosMoves.map((x) => x)
    for (let i = 0; i < p.length; i++) {game.move({from:p[i][0].toLowerCase(),to:p[i][1].toLowerCase()})}
    if (game.isGameOver()===true) {
        if (game.isStalemate()) {
            return 'Stalemate'
        } else {
            return true
        }
    } else {
        return false
    }
}

export {MoveSuccessful,isCheckmate}