from stockfish import Stockfish
from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from trainNeuralNetwork import trainNeuralNetwork
from translations import *
from createBoardLayout import createBoardLayout
import random
import chess
import threading

stockfish=Stockfish('api\stockfish.exe')

def DevTraining():
    print('here')
    defaultLayout=      [toFEN([['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]) + ' w KQkq - 0 0' , [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]]
    LightBregadeLayout= [toFEN([['MT', 'BQ', 'MT', 'BQ', 'BK', 'MT', 'BQ', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']]) + ' w - - 0 0'    , [['MT', 'BQ', 'MT', 'BQ', 'BK', 'MT', 'BQ', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']]]
    Horde=              [toFEN([['BP', 'BP', 'BP', 'BP', 'BK', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'BP', 'BP', 'MT', 'MT', 'BP', 'BP', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]) + ' w - - 0 0'    , [['BP', 'BP', 'BP', 'BP', 'BK', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'BP', 'BP', 'MT', 'MT', 'BP', 'BP', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]]
    PeasantsRevolt=     [toFEN([['MT', 'BN', 'BN', 'MT', 'BK', 'MT', 'BN', 'MT'],['MT', 'MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'WK', 'MT', 'MT', 'MT']]) + ' w KQkq - 0 0' , [['MT', 'BN', 'BN', 'MT', 'BK', 'MT', 'BN', 'MT'],['MT', 'MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'WK', 'MT', 'MT', 'MT']]]
    UpsideDown=         [toFEN([['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]) + ' w - - 0 0'    , [['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]]
    Weak=               [toFEN([['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'MT'],['MT', 'MT', 'WP', 'MT', 'MT', 'WP', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']]) + ' w KQ - 0 0'   , [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'MT'],['MT', 'MT', 'WP', 'MT', 'MT', 'WP', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']]]
    Layouts=[defaultLayout,LightBregadeLayout,Horde,PeasantsRevolt,UpsideDown,Weak]

    Layout=random.choice(Layouts)
    while stockfish.is_fen_valid(Layout[0])==False:
        Layout=random.choice(Layouts)
    stockfish.set_fen_position(Layout[0])
    board=chess.Board(Layout[0])
    listOfMoves=[]
    StartingLayout=Layout[1]
    count=0
    while board.outcome()==None:
        if count%2==0:
            m=stockfish.get_best_move()
            stockfish.make_moves_from_current_position([m])
            fen=board.fen()
            previosLayout=fromFENtoBoardLayout(fen)
            n = chess.Move.from_uci(m)
            board.push(n)
            fen=board.fen()
            currentLayout=fromFENtoBoardLayout(fen)
            tosquare,fromsquare,blank,flag='','','',False
            for j in range(0,8):    #finsing which piece moved and hoe it moved
                for i in range(0,8):
                    if currentLayout[j][i]!=previosLayout[j][i]:
                        if currentLayout[j][i]=='MT':
                            if flag==False:
                                fromsquare=toCoOrdinates([i,j])
                                piece=previosLayout[j][i]
                            else:
                                blank=toCoOrdinates([i,j])
                        else:
                            tosquare=toCoOrdinates([i,j])
            if flag==True and blank!='':
                if piece==currentLayout[toTuple(tosquare)[1]][toTuple(tosquare)[0]]:
                    move=[fromsquare,tosquare,blank]
                else:
                    piece=previosLayout[toTuple(blank)[1]][toTuple(blank)[0]]
                    move=[blank,tosquare,fromsquare]
            elif piece!=currentLayout[toTuple(tosquare)[1]][toTuple(tosquare)[0]]:
                move=[tosquare,fromsquare,currentLayout[toTuple(tosquare)[1]][toTuple(tosquare)[0]]]
            else:
                move=[tosquare,fromsquare]
            listOfMoves.append(move)
        else:
            moveLayout,coordiates,piece=generateAMoveToReturnToThePlayer(listOfMoves, StartingLayout)
            move=coordinates.lower()[0]+coordinates.lower()[1]
            if stockfish.is_move_correct(move)==False:
                m=stockfish.get_best_move()
                stockfish.make_moves_from_current_position([m])
                fen=board.fen()
                previosLayout=fromFENtoBoardLayout(fen)
                n = chess.Move.from_uci(m)
                board.push(m)
                fen=board.fen()
                currentLayout=fromFENtoBoardLayout(fen)
                tosquare,fromsquare,blank,flag='','','',False
                for j in range(0,8):    #finsing which piece moved and hoe it moved
                    for i in range(0,8):
                        if currentLayout[j][i]!=previosLayout[j][i]:
                            if currentLayout[j][i]=='MT':
                                if flag==False:
                                    fromsquare=toCoOrdinates([i,j])
                                    piece=previosLayout[j][i]
                                else:
                                    blank=toCoOrdinates([i,j])
                            else:
                                tosquare=toCoOrdinates([i,j])
                if flag==True and blank!='':
                    if piece==currentLayout[toTuple(tosquare)[1]][toTuple(tosquare)[0]]:
                        move=[fromsquare,tosquare,[blank]]
                        print(move)
                    else:
                        piece=previosLayout[toTuple(blank)[1]][toTuple(blank)[0]]
                        move=[blank,tosquare,[fromsquare]]
                        print(move)
                elif piece!=currentLayout[toTuple(tosquare)[1]][toTuple(tosquare)[0]]:
                    move=[tosquare,fromsquare,[currentLayout[toTuple(tosquare)[1]][toTuple(tosquare)[0]]]]
                    if move[2][0][1]=='K':
                        raise ValueError('wtf man ',move)
                else:
                    move=[tosquare,fromsquare]
                listOfMoves.append(move)
            else:
                stockfish.make_moves_from_current_position([move])
                n = chess.Move.from_uci(move)
                board.push(move)
                listOfMoves.append(coordinates)
    #print(listOfMoves)
    for i in range(1,len(listOfMoves)):
        try:
            createBoardLayout(StartingLayout, listOfMoves[0:i])
        except:
            raise  ValueError('move is ',listOfMoves[i],' and i is ',i,' and list of moves is ',listOfMoves)
            
    trainNeuralNetwork(StartingLayout,listOfMoves)

def task():
    while True:
        if event.is_set():
            break
        DevTraining()


event=threading.Event()
t=threading.Thread(None,task)

if len(input('are you sure you want to start?: '))<=0:
    DevTraining()
    #t.start()
    #input('stop?: ')
    #event.set()
    #t.join()
