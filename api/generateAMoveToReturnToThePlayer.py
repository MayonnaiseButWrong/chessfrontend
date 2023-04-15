from useStartingMoveEncyclopediaToGenerateResponseMove import useStartingMoveEncyclopediaToGenerateResponseMove
from useEndingTacticsToGenerateMove import useEndingTacticsToGenerateMove
from UseGenericTacticToGenerateMove import useMidgameTacticToGenerateMove
from createBoardLayout import createBoardLayout

def generateAMoveToReturnToThePlayer(listOfMoves,StartingLayout):
    if len(listOfMoves)<18:
        return useStartingMoveEncyclopediaToGenerateResponseMove(listOfMoves, StartingLayout)
    else:
        boardLayout=createBoardLayout(StartingLayout, listOfMoves)
        count=0
        for j in range(8):
            for i in range(8):
                if not boardLayout[j][i]=='MT':
                    count+=1
        if count<=7:
            return useEndingTacticsToGenerateMove(boardLayout)
        else:
            moveLayout,coordiates,piece=useMidgameTacticToGenerateMove(boardLayout, listOfMoves)
            return moveLayout,coordiates,piece