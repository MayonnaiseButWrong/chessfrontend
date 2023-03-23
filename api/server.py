from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from updateDatabase import updateDatabase
from translations import *
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/DailyChessdata')
def get_startingLayout():
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
        layout = request.args.get('answer')
        print(layout)
        startingLayout = [
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
        ['BP', 'BP', 'BP', 'MT', 'BP', 'BP', 'BP', 'BP'],
        ['MT', 'MT', 'MT', 'BP', 'MT', 'MT', 'MT', 'MT'],
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

if __name__ == '__main__':
    app.run(port=8080)
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