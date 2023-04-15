from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from multiprocessing import Pool
from NeuralNetwork4 import*
NNUE=NeuralNetwork([4*64,64,10])

maxDepth=2

def rateMoveBasedOnWinProbability(boardLayout,depth):
    p,q,pchange,qchange=0,0,0,0
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1,pieces)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2,pieces=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2,pieces)
        if len(bmoves)>0:
            if depth<maxDepth:
                for bmove in bmoves:
                    wImportantPieces3,bImportantPieces3,pieces=findImportantPieces(bmove)
                    checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3,pieces)
                    if len(checkMoves)==0:
                        p+=1
                    else:
                        depth+=1
                        pchange,qchange=rateMoveBasedOnWinProbability(bmove, depth)
            else:
                pool = Pool(6)
                pchanges=pool.map(NNUE.evaluate,bmoves)
                for change in pchanges:
                    qchange+=1
                    pchange+=change
    return p+pchange,q+qchange+1


