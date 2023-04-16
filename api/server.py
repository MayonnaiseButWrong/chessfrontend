from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from translations import *
from flask import Flask, jsonify, request
import psutil
from trainNeuralNetwork import*
import sys

app = Flask(__name__)

class Training:
    def __init__(self):
        self.trainingdata=[]
    
    def enterTrainingData(self,layout,movesList):
        self.trainingdata.append((layout,movesList))
        if psutil.cpu_percent(4)<50:
            map(trainNeuralNetwork,self.trainingdata)
        self.trainingdata=[]
        
training=Training()

@app.route('/EndGameChessdata', methods = ['GET'])
def get_EndGameChess_startingLayout():
    if request.method == 'GET':
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
        output=jsonify({
            'StaringLayoutString': startingLayout
        })
        return output

@app.route('/DailyChessdata', methods = ['GET'])
def get_DailyChess_startingLayout():
    if request.method == 'GET':
        startingLayout = [
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'WP', 'MT', 'WP'],
        ['WP', 'WP', 'WP', 'WP', 'WP', 'MT', 'WP', 'MT'],
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        ]
        output=jsonify({'StaringLayoutString': startingLayout})
        return output

@app.route('/moverequest', methods = ['POST'])
def move_request():
    if request.method == 'POST':
        StartingLayout = request.json.get('StartingLayout','alternative')
        listOfMoves = request.json.get('listofmoves','alternative')
        moveLayout,coordiates,piece=generateAMoveToReturnToThePlayer(listOfMoves, StartingLayout)
        output=jsonify({
            'NextLayout': moveLayout,
            'Coordiantes': coordiates,
            'Piece': piece
        })
        return output

@app.route('/outputgame', methods = ['PUT'])
def outputgame():
    if request.method == 'PUT':
        StartingLayout = request.json.get('StartingLayout')
        listOfMoves = request.json.get('listOfMoves')
        training.enterTrainingData(StartingLayout, listOfMoves)
        return''

if __name__ == '__main__':
    app.run(port=8080, debug=True)
