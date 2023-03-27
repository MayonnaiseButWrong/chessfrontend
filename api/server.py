from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from updateDatabase import updateDatabase
from translations import *
from flask import Flask, jsonify, request
import threading as t
from multiprocessing import Pool
from trainNeuralNetwork import*

app = Flask(__name__)

class Training:
    def __init__(self):
        self.trainingdata=[]
    
    def enterTrainingData(self,layout,movesList):
        self.trainingdata.append((layout,movesList))
        if t.active_count()<5:
            with Pool() as pool:
                pool.starmap(trainNeuralNetwork,self.trainingdata)
                pool.terminate()
        self.trainingdata=[]
        
training=Training()

@app.route('/EndGameChessdata')
def get_EndGameChess_startingLayout():
    startingLayout = [
        ['MT','WN','WN','WR','WR','WB','WB','WQ'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','BR','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','BK','MT'],
        ['BQ','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','BB','BN','BN','BB','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','BR'],
        ['MT','MT','MT','MT','MT','MT','WK','MT']
        ]
    startingstring = to_xenonnumber(startingLayout)
    print(type(startingstring))
    
    output=jsonify({
        'StaringLayoutString': startingLayout
    })
    print(output)
    return output

@app.route('/DailyChessdata', methods = ['GET'])
def get_DailyChess_startingLayout():
    if request.method == 'GET':
        print('here')
        startingLayout = [
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'WP', 'MT', 'MT'],
        ['WP', 'WP', 'WP', 'WP', 'WP', 'MT', 'WP', 'WP'],
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        ]
        startingstring = to_xenonnumber(startingLayout)
        print(type(startingstring))

        output=jsonify({
            'StaringLayoutString': startingLayout
        })
        print(output)
        return output

@app.route('/moverequest', methods = ['POST'])
def move_request():
    if request.method == 'POST':
        StartingLayout = request.args.get('StartingLayout')
        listOfMoves = request.args.get('listOfMoves')
        moveLayout,coordiates,piece=generateAMoveToReturnToThePlayer(listOfMoves, StartingLayout)
        #startingLayout = [
        #['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
        #['BP', 'BP', 'BP', 'MT', 'BP', 'BP', 'BP', 'BP'],
        #['MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT', 'MT'],
        #['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        #['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        #['MT', 'MT', 'MT', 'MT', 'MT', 'WP', 'MT', 'MT'],
        #['WP', 'WP', 'WP', 'WP', 'WP', 'MT', 'WP', 'WP'],
        #['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        #]

        output=jsonify({
            'NextLayout': moveLayout,
            'Coordiantes': coordiates,
            'Piece': piece
        })
        print(output)
        return output

@app.route('/outputgame', methods = ['PUT'])
def outputgame():
    if request.method == 'PUT':
        StartingLayout = request.args.get('StartingLayout')
        listOfMoves = request.args.get('listOfMoves')
        training.enterTrainingData(StartingLayout, listOfMoves)
        return''

if __name__ == '__main__':
    app.run(port=8080, debug=True)
#class move:
#    def __init__(self,StartingLayout,listOfMoves):
#        self.StartingLayout=to_gamelist(StartingLayout)
#        self.listOfMoves=stringToList(listOfMoves)
#        self.responseMove=generateAMoveToReturnToThePlayer(self.listOfMoves, self.StartingLayout)
#
#class game:
#    def __init__(self,StartingLayout,listOfMoves):
#        self.StartingLayout=StartingLayout
#        self.listOfMoves=stringToList(listOfMoves)
#    def DatabaseUpdate(self):
#        updateDatabase(self.StartingLayout,self.listOfMoves)

#concurrent futures:     https://docs.python.org/3/library/concurrent.futures.html
#multithreading:         https://www.geeksforgeeks.org/multithreading-python-set-1/

#moveObject=move(StartingLayout,listOfMoves)
#moveObject.returnMove()
#del moveObject

#gameObject=game(StartingLayout,listOfMoves)
#gameObject.returnMove()
#del gameObject