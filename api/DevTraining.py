from stockfish import Stockfish
from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from trainNeuralNetwork import trainNeuralNetwork
from translations import *
from createBoardLayout import createBoardLayout
import random
import chess
import threading

stockfish=Stockfish('api\stockfish.exe')

# allows the developer to train the NNUE and database

def DevTraining():
    print('here')
    defaultLayout=      [toFEN([['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]) + ' w KQkq - 0 0' , [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']],'defaultLayout']
    LightBregadeLayout= [toFEN([['MT', 'BQ', 'MT', 'BQ', 'BK', 'MT', 'BQ', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']]) + ' w - - 0 0'    , [['MT', 'BQ', 'MT', 'BQ', 'BK', 'MT', 'BQ', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']],'LightBregadeLayout']
    Horde=              [toFEN([['BP', 'BP', 'BP', 'BP', 'BK', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'BP', 'BP', 'MT', 'MT', 'BP', 'BP', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]) + ' w - - 0 0'    , [['BP', 'BP', 'BP', 'BP', 'BK', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'BP', 'BP', 'MT', 'MT', 'BP', 'BP', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']],'Horde']
    PeasantsRevolt=     [toFEN([['MT', 'BN', 'BN', 'MT', 'BK', 'MT', 'BN', 'MT'],['MT', 'MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'WK', 'MT', 'MT', 'MT']]) + ' w KQkq - 0 0' , [['MT', 'BN', 'BN', 'MT', 'BK', 'MT', 'BN', 'MT'],['MT', 'MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'WK', 'MT', 'MT', 'MT']],'PeasantsRevolt']
    UpsideDown=         [toFEN([['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]) + ' w - - 0 0'    , [['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']],'UpsideDown']
    Weak=               [toFEN([['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'MT'],['MT', 'MT', 'WP', 'MT', 'MT', 'WP', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']]) + ' w KQ - 0 0'   , [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'MT'],['MT', 'MT', 'WP', 'MT', 'MT', 'WP', 'MT', 'MT'],['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],['WN', 'WN', 'WN', 'WN', 'WK', 'WN', 'WN', 'WN']],'Weak']
    Layouts=[defaultLayout,LightBregadeLayout,Horde,PeasantsRevolt,UpsideDown,Weak]

    #Layout=random.choice(Layouts)
    #while stockfish.is_fen_valid(Layout[0])==False:
    #    Layout=random.choice(Layouts)
    #print(Layout[2])
    Layout=UpsideDown
    stockfish.set_fen_position(Layout[0])
    board=chess.Board(Layout[0])
    listOfMoves=[]
    StartingLayout=Layout[1]
    count=0
    while board.outcome()==None:
        print(count,'in game loop')
        print(Layout[2])
        if count%2==0:
            print('stockfish')
            moves=stockfish.get_top_moves(10)
            m=random.choice(moves)['Move']
            stockfish.make_moves_from_current_position([m])
            fen=board.fen()
            previosLayout=fromFENtoBoardLayout(fen)
            n = chess.Move.from_uci(m)
            board.push(n)
            move=[m[0].upper()+m[1],m[2].upper()+m[3]]
            if len(m)>4:
                move.append(['W'+m[4].upper()])
            elif previosLayout[toTuple(move[0])[1]][toTuple(move[0])[0]][1]=='P' and toTuple(move[0])[1]==4:
                if toTuple(move[1])[0]-toTuple(move[0])[0]>0 and previosLayout[toTuple(move[0])[1]][toTuple(move[0])[0]+1][1]=='P':
                    move.append([toCoOrdinates([toTuple(move[0])[0]+1,toTuple(move[0])[1]])])
                elif toTuple(move[1])[0]-toTuple(move[0])[0]<0 and previosLayout[toTuple(move[0])[1]][toTuple(move[0])[0]-1][1]=='P':
                    move.append([toCoOrdinates([toTuple(move[0])[0]-1,toTuple(move[0])[1]])])
            listOfMoves.append(move)
        else:
            print('ai')
            moveLayout,coordinates,piece=generateAMoveToReturnToThePlayer(listOfMoves, StartingLayout)
            move=coordinates[0].lower()+coordinates[1].lower()
            if stockfish.is_move_correct(move)==False:
                moves=stockfish.get_top_moves(10)
                m=random.choice(moves)['Move']
                stockfish.make_moves_from_current_position([m])
                fen=board.fen()
                previosLayout=fromFENtoBoardLayout(fen)
                n = chess.Move.from_uci(m)
                board.push(n)
                move=[m[0].upper()+m[1],m[2].upper()+m[3]]
                if len(m)>4:
                    move.append(['B'+m[4].upper()])
                elif previosLayout[toTuple(move[0])[1]][toTuple(move[0])[0]][1]=='P' and toTuple(move[0])[1]==3:
                    if toTuple(move[1])[0]-toTuple(move[0])[0]>0 and previosLayout[toTuple(move[0])[1]][toTuple(move[0])[0]+1][1]=='P':
                        move.append([toCoOrdinates([toTuple(move[0])[0]+1,toTuple(move[0])[1]])])
                    elif toTuple(move[1])[0]-toTuple(move[0])[0]<0 and previosLayout[toTuple(move[0])[1]][toTuple(move[0])[0]-1][1]=='P':
                        move.append([toCoOrdinates([toTuple(move[0])[0]-1,toTuple(move[0])[1]])])
                listOfMoves.append(move)
            else:
                stockfish.make_moves_from_current_position([move])
                n = chess.Move.from_uci(move)
                board.push(n)
                listOfMoves.append(coordinates)
        count+=2
    #print(listOfMoves)
    for i in range(1,len(listOfMoves)):
        try:
            createBoardLayout(StartingLayout, listOfMoves[0:i])
        except:
            raise  ValueError('move is ',listOfMoves[i-1:i+1],' and i is ',i,' and list of moves is ',listOfMoves)
            
    trainNeuralNetwork(StartingLayout,listOfMoves)

def task():
    while True:
        if event.is_set():
            break
        DevTraining()


event=threading.Event()
t=threading.Thread(None,task)

if len(input('are you sure you want to start?: '))<=0:
    for i in range(10):
        DevTraining()
        #t.start()
        #input('stop?: ')
        #event.set()
        #t.join()
