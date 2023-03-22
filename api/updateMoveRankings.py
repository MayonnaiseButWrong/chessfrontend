from createBoardLayout import createBoardLayout
from UseGenericTacticToGenerateMove import UseGenericTacticToGenerateMove
from translations import *

def updateMoveRankings(StartingLayout,listOfMoves):
    for count in range(listOfMoves):
        if count>0:
            move=createBoardLayout(listOfMoves[count], move)
        else:
            move=createBoardLayout(listOfMoves[count], StartingLayout)
        if count%2==0:
            move=mirrorBoard(move)
            for j in range(8):
                for i in range(8):
                    if not boardLayout[j][i]=='MT':
                        count+=1
            if count<=7:
                print('mdvko')
            else:
                #get best follow-up move from the mid-game move database
                #DatabaseMove=to_xenonnumber(move)
                newBestMove=UseGenericTacticToGenerateMove(move,listOfMoves)
                newBestMove=to_xenonnumber(move)
                #if not newBestMove is the same as move from mid-game movedatabase
                #update move in mid-game move database
