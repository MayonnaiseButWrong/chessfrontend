from createBoardLayout import createBoardLayout
from translations import *
import urllib3

http = urllib3.PoolManager()

def useEndingTacticsToGenerateMove(StartingLayout, listOfMoves):
    boardLayout=createBoardLayout(StartingLayout, listOfMoves)
    request=http.request('GET','http://tablebase.lichess.ovh/standard' + formatrequest(toFEN(boardLayout)))
    reply=request.data.decode('utf-8')
    try:
        output=formatoutput(reply)
    except:
        move,coordinates,piece=UseGenericTacticToGenerateMove(boardLayout, previosMovesList)
    else:
        uci=output['moves'][0]['uci']
        coordinates=[uci[0:2].upper(),uci[2:5].upper()]
        piece=boardLayout[toTuple(coordinates[0])[1]][toTuple(coordinates[0])[0]]
        move=createBoardLayout(StartingLayout.append(coordinates), listOfMoves)
    return move,coordinates,piece
