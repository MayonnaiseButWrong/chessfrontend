from createBoardLayout import createBoardLayout
from UseGenericTacticToGenerateMove import UseGenericTacticToGenerateMove
from translations import *
#import mysql.connector
#
#database = mysql.connector.connect(
#    host = 'localhost'
#)


def updateStartingMoveEncyclopaedia(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        if count%2==0:
            move=mirrorBoard(move)
            #if not found in online starting move databse
            #get best follow-up move from the starting move database
            #https://sourceforge.net/p/scidvspc/code/HEAD/tree/scid.eco 
            #its a text file so you have to translate the database before use, also you have to translate the thing that your searching for lol
            #DatabaseMove=to_xenonnumber(move)
            newBestMove=UseGenericTacticToGenerateMove(move,listOfMoves)
            newBestMove=to_xenonnumber(move)
            #if not newBestMove is the same as move from starting move database
            #update move in starting move database
    return move
