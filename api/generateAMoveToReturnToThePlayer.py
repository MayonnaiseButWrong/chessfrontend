from useStartingMoveEncyclopediaToGenerateResponseMove import useStartingMoveEncyclopediaToGenerateResponseMove
from useEndingTacticsToGenerateMove import useEndingTacticsToGenerateMove
from UseGenericTacticToGenerateMove import useMidgameTacticToGenerateMove
from createBoardLayout import createBoardLayout
import copy

def generateAMoveToReturnToThePlayer(listOfMoves,StartingLayout):   #returns the layout, coordinates and piece affected by the move made by the ai. it uses different functions of finding these values depending on the input provided
    if len(listOfMoves)<18: #if less that 188 total moves have been made, or a depth of 9 ply has been reached, then the starting moves database
        return useStartingMoveEncyclopediaToGenerateResponseMove(listOfMoves, StartingLayout)
    else:
        boardLayout=createBoardLayout(copy.deepcopy(StartingLayout), copy.deepcopy(listOfMoves))
        count=0
        for j in range(8):
            for i in range(8):
                if not boardLayout[j][i]=='MT':
                    count+=1
        if count<=7:    #if there are seven or less pieces on the board then it uses the ending
            return useEndingTacticsToGenerateMove(boardLayout, listOfMoves)
        else:   #if neither of the obove methods are possible it uses the midgame tactics
            moveLayout,coordiates,piece=useMidgameTacticToGenerateMove(boardLayout, listOfMoves)
            return moveLayout,coordiates,piece