from useStartingMoveEncyclopediaToGenerateResponseMove import useStartingMoveEncyclopediaToGenerateResponseMove
from useEndingTacticsToGenerateMove import useEndingTacticsToGenerateMove
from UseGenericTacticToGenerateMove import useMidgameTacticToGenerateMove
from createBoardLayout import createBoardLayout
import copy

def generateAMoveToReturnToThePlayer(listOfMoves,StartingLayout):
    #if len(listOfMoves)<18:
    #    return useStartingMoveEncyclopediaToGenerateResponseMove(listOfMoves, StartingLayout)
    #else:
    #    boardLayout=createBoardLayout(copy.deepcopy(StartingLayout), copy.deepcopy(listOfMoves))
    #    count=0
    #    for j in range(8):
    #        for i in range(8):
    #            if not boardLayout[j][i]=='MT':
    #                count+=1
    #    if count<=7:
    #        return useEndingTacticsToGenerateMove(boardLayout, listOfMoves)
    #    else:
    #        moveLayout,coordiates,piece=useMidgameTacticToGenerateMove(boardLayout, listOfMoves)
    #        return moveLayout,coordiates,piece
    boardLayout=createBoardLayout(copy.deepcopy(StartingLayout), copy.deepcopy(listOfMoves))
    return useMidgameTacticToGenerateMove(copy.deepcopy(StartingLayout),boardLayout, listOfMoves)