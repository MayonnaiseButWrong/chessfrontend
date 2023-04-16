from generateAMoveToReturnToThePlayer import generateAMoveToReturnToThePlayer
from createBoardLayout import createBoardLayout
from findImportantPieces import findImportantPieces
from generateMovesUsingImportantPieces import generatePossibleMovesUsingImportantPieces
from translations import *
from flask import Flask, jsonify, request
import psutil
from trainNeuralNetwork import*
import sys
import copy

#startingLayout = [
#        ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
#        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
#        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
#        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
#        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
#        ['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],
#        ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
#        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
#        ]

startingLayout=[['MT', 'MT', 'WK', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WQ', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'BB', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['WP', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'BP', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'WP', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT'],['MT', 'BK', 'MT', 'MT', 'MT', 'MT', 'MT', 'MT']]

listOfMoves = [['A4', 'B5'],['B1', 'B2'],['B5', 'B6'],['B2', 'B1'],['B6', 'B7'],['B1', 'B2'],['B7', 'B8',['WQ']],['B2', 'C3'],['A6', 'B6'],['C3', 'C4'],['B6', 'B3']]
#listOfMoves = [['A4', 'B5'],['B1', 'B2'],['B5', 'B6']]
boardLayout=createBoardLayout(copy.deepcopy(startingLayout), copy.deepcopy(listOfMoves))
#w,b,p=findImportantPieces(boardLayout)
#print('w',w,'b',b,'p',p)
#moves=generatePossibleMovesUsingImportantPieces(boardLayout, b, w, p)
#print(len(moves),'out')
#for a in moves:
#    print(toCoOrdinates(a[1][0]),toCoOrdinates(a[1][1]),'outs',a[1])

moveLayout,coordiates,piece=generateAMoveToReturnToThePlayer(listOfMoves, startingLayout)
for i in moveLayout:
    print(i)
print(coordiates)
print(piece)