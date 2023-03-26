from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from multiprocessing import Pool
#from ratingBasedOnNeuralNetwork import ratingBasedOnNeuralNetwork
from NeuralNetwork4 import*
import time
NNUE=NeuralNetwork([4*64,64,10])

maxDepth=2
#pool = Pool(250)

def rateMoveBasedOnWinProbability(boardLayout,depth,num):
    print('rate move depth',depth)
    p,q,pchange,qchange=0,0,0,0
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1,pieces)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2,pieces=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2,pieces)
        if len(bmoves)>0:
            p-=1
            print(len(wmoves),len(bmoves))
            for bmove in bmoves:
                wImportantPieces3,bImportantPieces3,pieces=findImportantPieces(bmove)
                checkMoves=generateMovesUsingImportantPieces(bmove, wImportantPieces3, bImportantPieces3,pieces)
                if len(checkMoves)==0:
                    p+=1
                elif depth<maxDepth:
                    depth+=1
                    pchange,qchange,num=rateMoveBasedOnWinProbability(bmove, depth,num)
                else:
                    num+=1
                    start_time = time.time()
                    pchange=NNUE.evaluate(bmove)
                    #print(time.time() - start_time,'time taken NNUE')
    return p+pchange,q+qchange+1,num


