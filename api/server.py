from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generateMovesUsingImportantPieces
from translations import *
from flask import Flask, jsonify, request
import psutil
from trainNeuralNetwork import*
import sys
import random
import datetime
import copy

app = Flask(__name__)

class Training:
    def __init__(self):
        self.trainingdata=[]
    
    def enterTrainingData(self,layout,movesList):
        self.trainingdata.append((layout,movesList))
        if psutil.cpu_percent(4)<50:
            map(trainNeuralNetwork,self.trainingdata)
        self.trainingdata=[]

def checkIfValid(layout):
    for i in range(8):
        if layout[0][i][1]=='P' or layout[7][i][1]=='P':
            return False
    vectors=[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9]],[[2,1]],[[1,2]],[[-2,1]],[[-1,2]],[[2,-1]],[[1,-2]],[[-1,-2]],[[-2,-1]]]
    for i in range(8):
        for j in range(8):
            if layout[j][i]=='BK':
                kingposition=[i,j]
                break
    
    if kingposition[0]-1>=0 and kingposition[1]+1<8 and layout[kingposition[1]-1][kingposition[0]-1]=='WP':
        return False
    if kingposition[0]+1<8 and kingposition[1]+1<8 and layout[kingposition[1]-1][kingposition[0]+1]=='WP':
        return False
    for direction in vectors:
        for vector in direction:
            if vector[1]+kingposition[1]<8 and vector[1]+kingposition[1]>=0 and vector[0]+kingposition[0]<8 and vector[0]+kingposition[0]>=0:
                if (vector[0]==1 or vector[1]==1) and layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]=='WK':
                    return False
                if abs(vector[0])==abs(vector[1]) and (layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]=='WQ' or layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]=='WB'):
                    return False
                elif (vector[0]==0 or vector[1]==0) and (layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]=='WQ' or layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]=='WR'):
                    return False
                elif layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]=='WN':
                    return False
    try:            
        wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(layout)
        moves=generateMovesUsingImportantPieces(layout, wImportantPieces1, bImportantPieces1,pieces)
        if len(moves)>0:
            return True
        else:
            return False
    except:
        return False

def generateStartingLayout():
    pieces=['B','N','R','P','P','P','P','Q']    #weighted so that pawns are four times more likely to bo chosen
    p=[False,False,False,False,False,True]
    white=['WK']
    black=['BK']
    isValid=False
    for i in range(random.randint(0,4)):
        white.append('W'+random.choice(pieces))
    for j in range(random.randint(0, 4)):
        black.append('B'+random.choice(pieces))
    while isValid==False:
        layout=[['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT']]
        w=copy.deepcopy(white)
        b=copy.deepcopy(black)
        while len(b)>0 or len(w)>0:
            for i in range(8):
                for j in range(8):
                    if layout[j][i]=='MT' and random.choice(p)==True and len(w)>0:
                        layout[j][i]=w.pop()
                    elif layout[j][i]=='MT' and random.choice(p)==True and len(b)>0:
                        layout[j][i]=b.pop()
        isValid=checkIfValid(layout)
    return layout

class DailyLayout:
    def __init__(self):
        self.createdDuringSetTime=False
        self.lastLayout=generateStartingLayout()
    
    def generateLayout(self):
        current = datetime.datetime.now()
        if current.hour>23:
            self.createdDuringSetTime=False
            return self.lastLayout
        if self.createdDuringSetTime==False:
            self.lastLayout=generateStartingLayout()
            return self.lastLayout

training=Training()
dailyLayout=DailyLayout()

@app.route('/EndGameChessdata', methods = ['GET'])
def get_EndGameChess_startingLayout():
    if request.method == 'GET':
        startingLayout = generateStartingLayout()
        output=jsonify({
            'StaringLayoutString': startingLayout
        })
        return output

@app.route('/DailyChessdata', methods = ['GET'])
def get_DailyChess_startingLayout():
    if request.method == 'GET':
        startingLayout=[['MT', 'MT', 'WK', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WQ', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'BB', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'BP', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'WP', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'BK', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT']]
        #startingLayout = dailyLayout.generateLayout()
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
