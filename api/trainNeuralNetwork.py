from concurrent.futures import ThreadPoolExecutor
from createBoardLayout import createBoardLayout
from stockfish import Stockfish
from translations import *
#from ratingBasedOnNeuralNetwork import NNUE
from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from NeuralNetwork4 import*
import time
import sys
#finding a way to constantly generate a dataset was out of the scope of this project, so i am just assuming that whatever stockish says is the best possible move and using that to train my own NNUE
stockfish=Stockfish('api\stockfish.exe')
NNUE=NeuralNetwork([4*64,64,10])
pool=ThreadPoolExecutor(100)
maxDepth=4

def tobinary(ins):
    out=[]
    print(ins)
    if ins<1:
        while ins<1:
            ins=ins*2
            out.append(0)
        out.append(1)
        for i in range(5):
            if ins>1: 
                out.append(1)
                ins-=1
            else: out.append(0)
        return out[1:-1]
    else:
        while ins>=1:
            out.append(ins%2)
            ins=ins//2
        while len(out)<4:
            out.append(0)
        return out[::-1]

def twoscompliment(ins):
    ins=tobinary(ins)
    flag,out=False,''
    for n in range(len(ins)):
        if n>len(ins):n=0
        if ins[-n]=='1' and flag==False:
            out='1'+out
            flag=True
        elif ins[-n]=='1':
            out='0'+out
        else:
            out='1'+out
    return out
        
def tomantissa(ins):
    ins=tobinary(ins)
    if len(ins)>6:
        exponent=len(ins)-6
        if exponent>14:
            exponent=twoscompliment(exponent)
            return exponent+ins[-7:-1]
        else:
            exponent=tobinary(exponent)
            return exponent+ins[-7:-1]
    else:
        return [0,0,0,0]+ins
    #fix this pls
    
def format(ins):
    out=[]
    if ins<0:
        a=tomantissa((float(100+int(ins))/100))
    else:
        a=tomantissa(float(int(ins)/100))
    for b in a:
        out.append([b])
    return out

def comparingProbabilities(boardLayout,depth):
    print('depth',depth)
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(boardLayout)
    wmoves=generateMovesUsingImportantPieces(boardLayout, wImportantPieces1, bImportantPieces1,pieces)
    for wmove in wmoves:
        wImportantPieces2,bImportantPieces2,pieces=findImportantPieces(wmove)
        bmoves=generateMovesUsingImportantPieces(wmove, bImportantPieces2, wImportantPieces2,pieces)
        if len(bmoves)<=0:
            continue
        else:
            prevmove=[]
            for bmove in bmoves:
                if bmove!=prevmove:
                    print('here 2 electric boogaloo',depth)
                    print(toFEN(bmove)+' b - - 0 1',stockfish.is_fen_valid(toFEN(bmove)+' b - - 0 1'))
                    fen=pool.submit(toFEN,bmove).result()+' b - - 0 1'
                    stockfish.set_fen_position(fen)
                    eval=stockfish.get_evaluation()
                    print(eval)
                    eval=format(eval['value'])
                    pool.submit(NNUE.train,[bmove,eval])
                    #NNUE.train([bmove,eval])
                    if depth<maxDepth:
                        depth+=1
                        comparingProbabilities(bmove, depth)
                prevmove=bmove
                    
def trainNeuralNetwork(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        comparingProbabilities(move, 0)

if __name__=="__main__":
    defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
    #isvalid=stockfish.is_fen_valid(toFEN(defaultLayout) + ' b - - 0 1')
    #if isvalid is True:
        #stockfish.set_fen_position(toFEN(defaultLayout) + ' b - - 0 1')
        #eval=stockfish.get_evaluation()
        #print(eval)
        #eval=format(eval['value'],numberofpoints(defaultLayout))
        #print(eval)
    #eval=format(22,numberofpoints(defaultLayout))
    #print(eval)
    #NNUE.train([defaultLayout,eval])
    #print('here')
    #start_time = time.time()
    print('starting in')
    time.sleep(0.25)
    print('3')
    time.sleep(0.25)
    print('2')
    time.sleep(0.25)
    print('1')
    time.sleep(0.25)
    print('go')
    sys.setrecursionlimit(10**6)
    print(sys.getrecursionlimit())
    comparingProbabilities(defaultLayout, 1)
    print('done')
    print("--- %s seconds ---" % (time.time() - start_time))