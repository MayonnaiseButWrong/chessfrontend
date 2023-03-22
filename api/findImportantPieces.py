from findWeights import findWeights

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
    weights=[['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT']]
    for j in range(8):
        for i in range(8):
            if (not boardLayout[j][i]=='MT') and weights[j][i]=='MT':
                weights=findWeights(boardLayout, [i,j], weights)
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
    while (wCount+bCount)<18:
        if boardLayout[sortedList[pieces][1]][sortedList[pieces][0]][0]=='W'and wCount<9:
            wImportantPieces.append(sortedList[pieces])
            wCount+=1
        elif bCount<9:
            bImportantPieces.append(sortedList[pieces])
            bCount+=1
        pieces+=1
    return wImportantPieces,bImportantPieces
            
                    