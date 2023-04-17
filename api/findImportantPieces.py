from findWeights import findWeights
from translations import *
import copy

def bubbleSort(seconadaryList,baseList):    #sorting the sedondary list based on the base list
    flag=True
    while flag==True:
        flag=False
        for count in range(1,len(baseList)):
            if baseList[count-1]<baseList[count]:
                temp1=baseList[count-1]
                temp2=seconadaryList[count-1]
                baseList[count-1]=baseList[count]
                seconadaryList[count-1]=seconadaryList[count]
                baseList[count]=temp1
                seconadaryList[count]=temp2
                flag=True
    return seconadaryList

def findImportantPieces(boardLayout):   #finds the important pieces and ranks them based on the board layout. returns the white and black important pieces seperately, along side the total number of pieces on the board
    #print(boardLayout,'findImportantPieces')
    weights=[['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT']]
    for j in range(8):
        for i in range(8):
            if (not boardLayout[j][i]=='MT') and weights[j][i]=='MT':
                weights=findWeights(copy.deepcopy(boardLayout), [i,j], weights)
    #print(boardLayout,'afterFindWeights')
    i,j=0,0
    listOfPieces=[]
    listOfWeights=[]
    for j in range(8):
        for i in range(8):
                if (not boardLayout[j][i]=='MT'):
                    listOfPieces.append([i,j])
                    listOfWeights.append(weights[j][i])
    #print('here')
    sortedList=bubbleSort(listOfPieces,listOfWeights)
    #print('there')
    wImportantPieces=[]
    bImportantPieces=[]
    wCount,bCount,pieces=0,0,0
    while (wCount+bCount)<8:
        if boardLayout[sortedList[pieces][1]][sortedList[pieces][0]][0]=='W':
            if wCount<4:
                wImportantPieces.append(sortedList[pieces])
                wCount+=1
        elif boardLayout[sortedList[pieces][1]][sortedList[pieces][0]][0]=='B':
            if bCount<4:
                bImportantPieces.append(sortedList[pieces])
                bCount+=1
        if (pieces+1<len(sortedList)):
            pieces+=1
        else:
            break
    return wImportantPieces,bImportantPieces,sortedList
                    