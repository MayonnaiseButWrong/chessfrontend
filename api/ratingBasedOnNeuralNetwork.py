import random
from NeuralNetwork4 import*

NNUE=NeuralNetwork([4*64,64,10])

def ratingBasedOnNeuralNetwork(boardLayout):
    return NNUE.evaluate(boardLayout)
    #you need a seperate file to initialise the neural network that isnt main, so that there isnt circular importing.
    #this function isnt strictly necessary, the neural network could have benn called directly, but this file needed more reaosons to exist