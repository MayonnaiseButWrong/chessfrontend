from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from createBoardLayout import createBoardLayout
from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generatePossibleMovesUsingImportantPieces
from translations import *
from flask import Flask, jsonify, request
import psutil
from trainNeuralNetwork import*
import sys

startingLayout = [
        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
        ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        ]

listOfMoves = [['G2', 'G4']]
['B8', 'A6'],
['G1', 'F3'],
['A8', 'B8'],
['F3', 'E5'],
['B8', 'A8'],
['G4', 'G5'],
['A8', 'B8'],
['G5', 'G6'],
['B8', 'A8'],
['G6', 'F7']

#boardLayout=createBoardLayout(startingLayout, listOfMoves)
#w,b,p=findImportantPieces(boardLayout)
#moves=generatePossibleMovesUsingImportantPieces(boardLayout, b, w, p)
#print(len(moves))
#for a in moves:
#    print(toCoOrdinates(a[1][0]),toCoOrdinates(a[1][1]),'outs',a[1])


moveLayout,coordiates,piece=generateAMoveToReturnToThePlayer(listOfMoves, startingLayout)
for i in moveLayout:
    print(i)
print(coordiates)
print(piece)