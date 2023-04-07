from UseGenericTacticToGenerateMove import UseGenericTacticToGenerateMove
from createBoardLayout import createBoardLayout
from translations import *
import sqlite3

ChessDb = sqlite3.connect('api\ChessData')
cursor = ChessDb.cursor()

try:
    cursor.execute("SELECT * FROM StartingMoves WHERE XenonNumber = '0x2ab3d08eeb5884825a2fc6594f9764d52bedae177a6bff2054eb124de618a3a8f0ac36e6c260c955da8c51954194fc8e89ad439b93d217376a89a95a7ef3d359947dc646e6d8d23fe21faec302013ea2b6a04534a5a7ed810feb47c787470ddd699473a9ce29d6e49494b2f603a413f2b4459779996183dc06d4a224776a53ec69fb5589eb59611b295673e0603ee5273ec11f6c2a0bf6628026f20080'")
    res=cursor.fetchall()
    print(res)
    if len(res)<=0:
        raise ValueError('No Data')
except:
    cursor.execute('DROP TABLE StartingMoves')
    cursor.execute('CREATE TABLE StartingMoves (XenonNumber VARCHAR(80), BestMovesXenonNumber VARCHAR(80), Piece CHAR(2), Move VARCHAR(6), Rating FLOAT, PRIMARY KEY(XenonNumber, BestMovesXenonNumber))')
    
    
    
    #*********************************************************************************************************************************************************************************************************************#> The parts between these markers are not all my work, a lot of this is from https://sourceforge.net/p/scidvspc/code/HEAD/tree/scripts/eco2pgn.py and  https://www.geeksforgeeks.org/extract-data-from-pgn-files-using-the-chess-library-in-python/ 
    import re
    import chess
    import chess.pgn
    from io import StringIO
    import sys
    fd=open('api\scid.eco','r')
    count=0
    while True:
        sys.stdout.write('\r'+str(count))
        count+=1
        board=chess.Board()
        line=fd.readline()
        if not line:break
        line = line[:-1]

        if re.match("\s*(#|$)", line): continue

        match = re.match("(\S+)\s+\"([^\"]+)\"(\s+.+)?$", line) #formatting the text from the file into the chess pgn format
        if match:
            eco, variation, cont = match.groups()

            if not cont:
                cont = ''

            while not cont or cont[-1] != '*':
                cont = cont + ' ' + fd.readline()[:-1]

            if cont[-1] == '*' and cont[-2] != ' ':
                cont = cont[:-1] + ' *'
            
            pgn=StringIO(cont)
            game=chess.pgn.read_game(pgn)   #translating the pgns into moves
            previosLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
            previosxenonnumber=to_xenonnumber(previosLayout)
            for number,move in enumerate(game.mainline_moves()):
                m=move.uci()
                board.push(move)    #moveing the move ont the board
                fen=board.fen()
                currentLayout=fromFENtoBoardLayout(fen)
                currentxenonnumber=to_xenonnumber(currentLayout)
                move=m[0].upper()+m[1]+m[2].upper()+m[3]
                if len(m)>4:
                    move=move+'B'+m[4].upper()
                elif previosLayout[toTuple(move[0:2])[1]][toTuple(move[0:2])[0]][1]=='P' and toTuple(move[0:2])[1]==3:
                    if toTuple(move[2:])[0]-toTuple(move[0:2])[0]>0 and previosLayout[toTuple(move[0:2])[1]][toTuple(move[0:2])[0]+1][1]=='P':
                        move=move+toCoOrdinates([toTuple(move[0:2])[0]+1,toTuple(move[0:2])[1]])
                    elif toTuple(move[2:])[0]-toTuple(move[0:2])[0]<0 and previosLayout[toTuple(move[0:2])[1]][toTuple(move[0:2])[0]-1][1]=='P':
                        move=move+toCoOrdinates([toTuple(move[0:2])[0]-1,toTuple(move[0:2])[1]])
                piece=previosLayout[toTuple(move[0:2])[1]][toTuple(move[0:2])[0]]
                cursor.execute("SELECT * FROM StartingMoves WHERE XenonNumber = '"+previosxenonnumber+"' AND BestMovesXenonNumber = '"+currentxenonnumber+"'")  #checking ig the record is already in the database, so that there is no duplicate data
                if len(cursor.fetchall())<=0:
                    params=(previosxenonnumber,currentxenonnumber,piece,move,0)
                    cursor.execute('INSERT INTO StartingMoves VALUES(?,?,?,?,?)',params)    #writing to the database
                previosxenonnumber=currentxenonnumber
                previosLayout=currentLayout
    #cursor.execute("SELECT * FROM StartingMoves WHERE XenonNumber = '0x2ab3d08eeb5884825a2fc6594f9764d52bedae177a6bff2054eb124de618a3a8f0ac36e6c260c955da8c51954194fc8e89ad439b93d217376a89a95a7ef3d359947dc646e6d8d23fe21faec302013ea2b6a04534a5a7ed810feb47c787470ddd699473a9ce29d6e49494b2f603a413f2b4459779996183dc06d4a224776a53ec69fb5589eb59611b295673e0603ee5273ec11f6c2a0bf6628026f20080'")
    #res=cursor.fetchall()
    #print(res)
cursor.close()
    #*********************************************************************************************************************************************************************************************************************# <

def useStartingMoveEncyclopediaToGenerateResponseMove(listOfMoves,StartingLayout):
    ChessDb = sqlite3.connect('api\ChessData')
    cursor = ChessDb.cursor()
    defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
    boardLayout=createBoardLayout(StartingLayout, listOfMoves)
    if StartingLayout == defaultLayout:
        boardLayout=createBoardLayout(StartingLayout, listOfMoves)
        cursor.execute('SELECT BestMoveXenonNumber,Move,Piece,TimesUsed FROM StartingMoves WHERE XenonNumber = "'+to_xenonnumber(boardLayout)+'" ORDER BY Rating')
        result = cursor.fetchall()
        if len(result)>=0:
            move=to_gamelist(result[0][0])
            c=result[0][1]
            coordinates=[c[0:1],c[2:3]]
            if len(c)>4:
                coordinates.append(c[4:5])
            cursor.close()
            return move, coordinates, result[0][2]
        else:
            boardLayout=createBoardLayout(StartingLayout, listOfMoves)
            return UseGenericTacticToGenerateMove(boardLayout,listOfMoves)
    else:
        boardLayout=createBoardLayout(StartingLayout, listOfMoves)
        return UseGenericTacticToGenerateMove(boardLayout,listOfMoves)
