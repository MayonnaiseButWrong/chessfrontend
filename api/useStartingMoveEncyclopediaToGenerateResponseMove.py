from UseGenericTacticToGenerateMove import UseGenericTacticToGenerateMove
from createBoardLayout import createBoardLayout

def useStartingMoveEncyclopediaToGenerateResponseMove(listOfMoves,StartingLayout):
    print('rwbgmomk')
    defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
    if StartingLayout == defaultLayout:
        boardLayout=createBoardLayout(StartingLayout, listOfMoves)
        #use chess openings database from online
    else:
        print('hi')
        #use built in database
    #if not in built in database
    boardLayout=createBoardLayout(StartingLayout, listOfMoves)
    move=UseGenericTacticToGenerateMove(boardLayout, previosMovesList)
    return move
