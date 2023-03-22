from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from updateDatabase import updateDatabase
from translations import *

class move:
    def __init__(self,StartingLayout,listOfMoves):
        self.StartingLayout=to_gamelist(StartingLayout)
        self.listOfMoves=stringToList(listOfMoves)
        self.responseMove=generateAMoveToReturnToThePlayer(self.listOfMoves, self.StartingLayout)

class game:
    def __init__(self,StartingLayout,listOfMoves):
        self.StartingLayout=StartingLayout
        self.listOfMoves=stringToList(listOfMoves)
    def DatabaseUpdate(self):
        updateDatabase(self.StartingLayout,self.listOfMoves)

#concurrent futures:     https://docs.python.org/3/library/concurrent.futures.html
#multithreading:         https://www.geeksforgeeks.org/multithreading-python-set-1/

#moveObject=move(StartingLayout,listOfMoves)
#moveObject.returnMove()
#del moveObject

#gameObject=game(StartingLayout,listOfMoves)
#gameObject.returnMove()
#del gameObject