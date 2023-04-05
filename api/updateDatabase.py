import sqlite3

def updateDatabase(XenonNumber,BestMoveXenonNumber,Rating,pieces,piece,move):
    ChessDb = sqlite3.connect('api\ChessData')
    cursor = ChessDb.cursor()
    if pieces>7:
        cursor.execute("SELECT * FROM StartingMoves WHERE XenonNumber = '"+XenonNumber+"' AND BestMovesXenonNumber = '"+BestMoveXenonNumber+"'")
        if len(cursor.fetchall())>0:
            cursor.execute('UPDATE StartingMoves SET Rating = '+str(Rating)+' WHERE  XenonNumber = "'+XenonNumber+'" AND BestMoveXenonNumber = "'+BestMoveXenonNumber+'"')
        else:
            cursor.execute('SELECT BestMoveXenonNumber,Move,Piece FROM BestMoves WHERE XenonNumber = ',to_xenonnumber(boardLayout),' ORDER BY Rating')
            if len(cursor.fetchall())>0:
                cursor.execute('UPDATE BestMoves SET Rating = '+str(Rating)+' WHERE  XenonNumber = "'+XenonNumber+'" AND BestMoveXenonNumber = "'+BestMoveXenonNumber+'"')
            else:
                params=(XenonNumber,BestMoveXenonNumber,piece,move,Rating)
                cursor.execute('INSERT INTO BestMoves VALUES(?,?,?,?,?)',params)
    cursor.close()