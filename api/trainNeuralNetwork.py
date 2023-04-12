from createBoardLayout import createBoardLayout
from translations import *
from rateMoveBasedOnWinProbability import rateMoveBasedOnWinProbability
from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from updateDatabase import updateDatabase
from NeuralNetwork4 import*
import time
import sys

#finding a way to constantly generate a dataset was out of the scope of this project, so i am just assuming that whatever stockish says is the best possible move and using that to train my own NNUE
from stockfish import Stockfish
stockfish=Stockfish('api\stockfish.exe')
stockfish.set_skill_level(20) #max skill
stockfish.set_depth(10)

NNUE=NeuralNetwork([4*64,64,10])
maxDepth=1

def tobinary(ins):
    out=[]
    if ins<1:
        while ins<1:
            print(ins)
            ins=ins*2
            out.append(0)
        out.append(1)
        for i in range(5):
            if ins>1: 
                out.append(1)
                ins-=1
            else: out.append(0)
        return out[1:]
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
    if ins==0:
        return[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    a=tomantissa(float((-ins)))
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
                    fen=toFEN(bmove)+' b - - 0 1'
                    stockfish.set_fen_position(fen)
                    print('moved stockfish')
                    evaluation=stockfish.get_top_moves(1)
                    print('eval',evaluation)
                    evaluation=evaluation[0]['Mate']
                    if evaluation==None:
                        evaluation=0
                    else:
                        evaluation=format(1/evaluation)
                    print('formatted evaluation',evaluation)
                    print('before')
                    NNUE.train([bmove,evaluation])
                    print('after')
                    if depth<maxDepth:
                        depth+=1
                        comparingProbabilities(bmove, depth)
                prevmove=bmove
                    
def trainNeuralNetwork(StartingLayout,listOfMoves):
    for count in range(len(listOfMoves)):
        #print(count,listOfMoves[0:count+1])
        move=createBoardLayout(StartingLayout, listOfMoves[0:count+1])
        #print(move)
        comparingProbabilities(move, 0)
    count,previosMove=0,[]
    #print('')
    for count in range(len(listOfMoves)):
        if count>0:
            move=createBoardLayout(move, listOfMoves[0:count+1])
            count=0
            for j in range(8):
                for i in range(8):
                    if not move[j][i]=='MT':
                        count+=1
            #updateDatabase(to_xenonnumber(previosMove),to_xenonnumber(move),rateMoveBasedOnWinProbability(move, 0),count,previosMove[toTuple(listOfMoves[count][0])[1]][toTuple(listOfMoves[count][0])[0]],listOfMoves[count])
            previosMove=move
        else:
            previosMove=createBoardLayout(StartingLayout, listOfMoves[0:count+1])
    
if __name__=="__main__":
    #defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
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
    #print('starting in')
    #time.sleep(0.25)
    #print('3')
    #time.sleep(0.25)
    #print('2')
    #time.sleep(0.25)
    #print('1')
    #time.sleep(0.25)
    #print('go')
    #sys.setrecursionlimit(10**6)
    #print(sys.getrecursionlimit())
    #comparingProbabilities(defaultLayout, 1)
    #print('done')
    #print("--- %s seconds ---" % (time.time() - start_time))
    print(format(31.97))