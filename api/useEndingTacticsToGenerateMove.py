from createBoardLayout import createBoardLayout

def useEndingTacticsToGenerateMove(boardLayout):
    #if there are 7 or less pieces left on the board, use the end game table base at https://syzygy-tables.info/ 
    #if its not found there use the normal database
    #if its not found in either, gerate a move
    boardLayout=createBoardLayout(StartingLayout, listOfMoves)
    move=UseGenericTacticToGenerateMove(boardLayout, previosMovesList)
    return move
