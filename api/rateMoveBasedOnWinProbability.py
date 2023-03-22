from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from ratingBasedOnNeuralNetwork import ratingBasedOnNeuralNetwork

maxDepth=12

def rateMoveBasedOnWinProbability(boardLayout,depth):
    p,q,pchange,qchange=0,0,0,0
    wImportantPieces1,bImportantPieces1=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2)
        if len(bmoves)>0:
            p-=1
        else:
            for bmove in bmoves:
                wImportantPieces3,bImportantPieces3=findImportantPieces(wmove)
                checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3)
                if len(checkMoves)>0:
                    p+=1
                elif depth<maxDepth:
                    depth+=1
                    pchange,qchange=rateMoveBasedOnWinProbability(bmove, depth)
                else:
                    pchange,qchange=ratingBasedOnNeuralNetwork(bmove)
    return p+pchange,q+qchange+1
