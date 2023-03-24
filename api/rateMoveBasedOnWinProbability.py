from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from ratingBasedOnNeuralNetwork import ratingBasedOnNeuralNetwork

maxDepth=10

def rateMoveBasedOnWinProbability(boardLayout,depth):
    print(depth)
    p,q,pchange,qchange=0,0,0,0
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1,pieces)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2,pieces=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2,pieces)
        if len(bmoves)>0:
            p-=1
        else:
            for bmove in bmoves:
                wImportantPieces3,bImportantPieces3,pieces=findImportantPieces(wmove)
                checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3,pieces)
                if len(checkMoves)>0:
                    p+=1
                elif depth<maxDepth:
                    depth+=1
                    pchange,qchange=rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    pchange,qchange=ratingBasedOnNeuralNetwork(bmove)
    return p+pchange,q+qchange+1
