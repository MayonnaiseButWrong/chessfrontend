from findWeights import findWeights
import copy

def bubbleSort(seconadaryList,baseList):
    flag=True
    while flag==True:
        flag=False
        for count in range(1,len(baseList)):
            if baseList[count-1]>baseList[count]:
                temp1=baseList[count-1]
                temp2=seconadaryList[count-1]
                baseList[count-1]=baseList[count]
                seconadaryList[count-1]=seconadaryList[count]
                baseList[count]=temp1
                seconadaryList[count]=temp2
                flag=True
    return seconadaryList

def findImportantPieces(boardLayout):
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
    sortedList=bubbleSort(listOfPieces,listOfWeights)
    wImportantPieces=[]
    bImportantPieces=[]
    wCount,bCount,pieces=0,0,0
    while (wCount+bCount)<8:
        print(len(sortedList),'sortedList',sortedList)
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
    #print(boardLayout[bImportantPieces[0][1]][bImportantPieces[0][0]],boardLayout[wImportantPieces[0][1]][wImportantPieces[0][0]],boardLayout[sortedList[0][1]][sortedList[0][0]])
    return wImportantPieces,bImportantPieces,sortedList
            
                    