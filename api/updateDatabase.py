from updateStartingMoveEncyclopaedia import updateStartingMoveEncyclopaedia
from updateMoveRankings import updateMoveRankings
from trainNeuralNetwork import trainNeuralNetwork

def updateDatabase(StartingLayout,listOfMoves):
    trainNeuralNetwork(StartingLayout,listOfMoves)
    move=updateStartingMoveEncyclopaedia(StartingLayout,listOfMoves)
    updateMoveRankings(move,listOfMoves)
