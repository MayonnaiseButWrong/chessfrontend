import time
from concurrent.futures import ThreadPoolExecutor
from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generatePossibleMovesUsingImportantPieces
from rateMoveBasedOnWinProbability import rateMoveBasedOnWinProbability
from createBoardLayout import createBoardLayout
from translations import *
from concurrent.futures import ThreadPoolExecutor
import sqlite3
import copy

ChessDb = sqlite3.connect('api\ChessData')
cursor = ChessDb.cursor()

try:
    cursor.execute("SELECT * FROM BestMoves WHERE XenonNumber = '0x2ab3d08eeb5884825a2fc6594f9764d52bedae177a6bff2054eb124de618a3a8f0ac36e6c260c955da8c51954194fc8e89ad439b93d217376a89a95a7ef3d359947dc646e6d8d23fe21faec302013ea2b6a04534a5a7ed810feb47c787470ddd699473a9ce29d6e49494b2f603a413f2b4459779996183dc06d4a224776a53ec69fb5589eb59611b295673e0603ee5273ec11f6c2a0bf6628026f20080'")
except:
    try:
        cursor.execute('CREATE TABLE BestMoves (XenonNumber VARCHAR(80), BestMovesXenonNumber VARCHAR(80), Piece CHAR(2), Move VARCHAR(6), Rating FLOAT, PRIMARY KEY(XenonNumber, BestMovesXenonNumber))')
    except:
        print('database is locked')

cursor.close()

pool = ThreadPoolExecutor(6)

def multiListBubbleSort(l1,l2,l3,b):    #base list=>b dependant lists=>l1,l2,l3
    flag=True
    while flag==True:
        flag=False
        for i in range(1,len(b)):
            if b[i-1]>b[i]:
                flag=True
                temp=b[i-1]
                b[i-1]=b[i]
                b[i]=b[i-1]
                temp=l1[i-1]
                l1[i-1]=l1[i]
                l1[i]=l1[i-1]
                temp=l2[i-1]
                l2[i-1]=l2[i]
                l2[i]=l2[i-1]
                temp=l3[i-1]
                l3[i-1]=l3[i]
                l3[i]=l3[i-1]
    return l1,l2,l3
            
    

def typeOfMove(layout1,layout2):    #0 is a mormal move, 1 is castling, 2 is enpassant
    if layout1[0][4]=='K' and layout2[0][4]=='MT':
        if layout2[0][6]=='BK':
            return 1,0
        elif layout2[0][2]=='BK':
            return 1,0
        else:
            return 0,0
                    
    for i in range(8):
        if not (layout1[4][i]=='MT'and layout1[4][i][0]=='W'):
            if layout1[4][i]=='P' and layout2[4][i]=='MT':
                if layout2[5][i]=='BP':
                    return 0,0
                elif i<7 and layout2[5][i+1]=='BP':
                    return 0,0
                elif i>0 and layout2[5][i-1]=='BP':
                    return 0,0
                else:
                    return 2,i
    return 0,None
                            
def castlingAllowed(previosMovesList):
    for move in previosMovesList:
        if move[0]==[4,0]:
            return False
        if move[0]==[0,0]:
            return False
        if move[0]==[7,0]:
            return False
    return True

def enPassantAllowed(previosMovesList,i):
    for move in previosMovesList:
        if i<7 and move[0]==[i+1,6] and move[1]==[i+1,4]:
            return True
        if i>0 and move[0]==[i-1,6] and move[1]==[i-1,4]:
            return True
    return False

def useMidgameTacticToGenerateMove(boardLayout,previosMovesList):
    ChessDb = sqlite3.connect('api\ChessData')
    cursor = ChessDb.cursor()
    try:
        cursor.execute('SELECT BestMovesXenonNumber,Move,Piece FROM BestMoves WHERE XenonNumber = "'+str(to_xenonnumber(boardLayout))+'"')
        result = cursor.fetchall()
        cursor.close()
        if len(result)>=0:
            move=to_gamelist(result[0][0])
            c=result[0][1]
            coordinates=[c[0:1],c[2:3]]
            if len(c)>4:
                coordinates.append(c[4:5])
            return move, coordinates, result[0][2]
    except:
        return UseGenericTacticToGenerateMove(copy.deepcopy(boardLayout),previosMovesList)

def UseGenericTacticToGenerateMove(boardLayout,previosMovesList):
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(copy.deepcopy(boardLayout))
    m=pool.submit(generatePossibleMovesUsingImportantPieces,copy.deepcopy(boardLayout), bImportantPieces1, wImportantPieces1,pieces)
    pValues,moves,coordinates,coordinate,pieces=[],[],[],[],[]
    for o in m.result():
        moves.append(o[0])
        pieces.append(boardLayout[o[1][0][1]][o[1][0][0]])
        coordinate.append(toCoOrdinates(o[1][0]))
        coordinate.append(toCoOrdinates(o[1][1]))
        if len(o[1])>2:
            if o[1][2][0][0]=='W' or o[1][2][0][0]=='B':
                coordinate.append(o[1][2])
            else:
                coordinate.append([toCoOrdinates(o[1][2][0])])
        coordinates.append(coordinate)
        coordinate=[]
    for move in moves:
        p,q=rateMoveBasedOnWinProbability(move,0)
        pValues.append(p*100000/q)
    coordinates,pieces,moves=multiListBubbleSort(coordinates,pieces,moves,pValues)
    flag=True
    count=0
    for count in range(len(moves)):
        moveType,i=typeOfMove(boardLayout,moves[count])
        if moveType==1:
            if castlingAllowed(previosMovesList)==True:
                return moves[count],coordinates[count],pieces[count]
            else:
                continue
        elif moveType==2:
            if enPassantAllowed(previosMovesList,i)==True:
                return moves[count],coordinates[count],pieces[count]
            else:
                continue
        else:
            return moves[count],coordinates[count],pieces[count]

if __name__=='__main__':
    defaultLayout=[
        ['MT','WN','WN','WR','WR','WB','WB','WQ'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','BR','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','BK','MT'],
        ['BQ','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','BB','BN','BN','BB','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','BR'],
        ['MT','MT','MT','MT','MT','MT','WK','MT']]
    previosMovesList=[['E2','E3']]
    print(toFEN(defaultLayout))
    print('starting in')
    time.sleep(0.25)
    print('3')
    time.sleep(0.25)
    print('2')
    time.sleep(0.25)
    print('1')
    time.sleep(0.25)
    print('go')
    start_time = time.time()
    move=UseGenericTacticToGenerateMove(createBoardLayout(defaultLayout, previosMovesList), previosMovesList)
    print(move)
    print('done')
    print("--- %s seconds ---" % (time.time() - start_time))