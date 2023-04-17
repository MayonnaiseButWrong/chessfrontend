from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from NeuralNetwork4 import*
NNUE=NeuralNetwork([4*64,64,10])

maxDepth=1

def rateMoveBasedOnWinProbability(boardLayout,depth):
    p,q,pchange,qchange=0,0,0,0
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1,pieces) #find the moves made by white
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2,pieces=findImportantPieces(wmove)#find the moves made by black
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2,pieces)
        if len(bmoves)>0:
            p-=1
            for bmove in bmoves:
                wImportantPieces3,bImportantPieces3,pieces=findImportantPieces(bmove)#see if its checkmate
                checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3,pieces)
                if len(checkMoves)==0:
                    p+=1
                elif depth<maxDepth:
                    depth+=1
                    pchange,qchange=rateMoveBasedOnWinProbability(bmove, depth)#recursivly rates this depth based on the next depth
                else:
                    pchange=NNUE.evaluate(bmove)#when the mad depth is reached the nnue is evalued to find the rating of a given layout
    return p+pchange,q+qchange+1


