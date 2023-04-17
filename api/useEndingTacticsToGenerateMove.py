from createBoardLayout import createBoardLayout
from UseGenericTacticToGenerateMove import UseGenericTacticToGenerateMove
from translations import *
import urllib3
import copy

http = urllib3.PoolManager()

def useEndingTacticsToGenerateMove(StartingLayout, listOfMoves):
    boardLayout=createBoardLayout(copy.deepcopy(StartingLayout), copy.deepcopy(listOfMoves))
    request=http.request('GET','http://tablebase.lichess.ovh/standard' + formatrequest(toFEN(boardLayout)))
    reply=request.data.decode('utf-8')
    try:
        output=formatoutput(reply)
        uci=output['moves'][0]['uci']
        coordinates=[uci[0:2].upper(),uci[2:5].upper()]
        piece=boardLayout[toTuple(coordinates[0])[1]][toTuple(coordinates[0])[0]]
        move=createBoardLayout(StartingLayout.append(coordinates), listOfMoves)
    except:
        move,coordinates,piece=UseGenericTacticToGenerateMove(boardLayout, previosMovesList)
    return move,coordinates,piece
