
def to_xenonnumber(gamelist):

    primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    Pieceslist=['MT','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    xenonnumber=1
    n1=0                                                                                              #announcing variables
    n2=0
    n3=0

    for j in range(0,8):                                                                               #there is garunteed to be 36 items in the game list inputted and we need to translate all of them
        for i in range(0,8):
            n1=int(primeNumbers[i*j])                                                                       #getting the actual numbers needed for the calculation from the list that they're in
            n2=int(Pieceslist.index(gamelist[j][i]))

            n3=n1**n2                                                                                     #the respective prime number to the power of the xenon number for the piece at the corresponding place, multiplied by all the others goves the unique xenon number for the frame
            xenonnumber=xenonnumber*n3

    xenonnumber="{:,f}".format(int(xenonnumber))
    outputstring=''
    for letter in xenonnumber:
        if letter!=','or letter!='.':
            outputstring+=letter
    return outputstring

def to_gamelist(xenonnumber):

    primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    Pieceslist=['MT','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    gamelist=[]                                                                                      #announcing the variables
    direction=[]
    n2=0
    numcount=0
    Piece=''

    for i in range (64):

        n2=primeNumbers[i]                                                                              #getting the corresponging number reqired from a list

        numcount=0

        while xenonnumber%n2==0:                                                                         #finding out how many of these are in the xenon number

            numcount+=1                                                                                 #the prime factorisation of the xenon number corresponds to the piece at the square corresponding to the prime number used. the prime numbers are tested from smalled to lagest resulting in the pieces from A1 to H8 on the chess board in order
            xenonnumber=xenonnumber//n2
        Piece=Pieceslist[numcount]                                                                       #translating the piece xenon number to the piece it corresponds to
        direction.append(Piece)
        if i%8==0 and i!=0:
            gamelist.append(direction)
            direction=[]
    return gamelist

def toCoOrdinates(inputTuple):
    letters=['A','B','C','D','E','F','G','H']
    return letters[(inputTuple[0])]+str(8-inputTuple[1])

def toTuple(InputCoOrdinates):
    letters=['A','B','C','D','E','F','G','H']
    return [int(letters.index(InputCoOrdinates[0])),8-int(InputCoOrdinates[1])]

def listToString(inputList):
    outputList=[]
    outputstr=''
    chars=['A','B','C','D','E','F','G','H','K','Q','N','M','R','P','T','W','0','1','2','3','4','5','6','7',',']
    for l in inputList:
        s=l[0]+l[1]
        if len(l)==3:
            l2=l[2]
            for count in range(len(l2)):
                s+=l2[count]
        outputList.append(s)
        
    for l in outputList:
        for count in range(len(l)):
            i=chars.index(l[count])
            if i<10:
                i='0'+str(i)
            else:
                i=str(i)
            outputstr+=i
    return outputstr

def stringToList(inputString):
    chars=['A','B','C','D','E','F','G','H','K','Q','N','M','R','P','T','W','0','1','2','3','4','5','6','7',',']
    outputstr=''
    outputlist=[]
    l=[]
    flag=-1
    s=''
    for count in range(len(inputString)):
        if not count%2:
            index=inputString[count]
            outputstr+=chars[index]
    
    for count in range(len(outputstr)):
        if outputlist[count]==',':
            for i in range(count-flag-1):
                s+=outputlist[i+flag]
                l.append(s)
            flag=count
    
    outputlist=[]
    for count in range(len(l)):
            if len(l[count])==4:
                outputlist.append([l[count][0]+l[count][1],l[count][2]+l[count][3]])
            else:
                tempList=[]
                for i in range(5,len(l[count])):
                    if not i%2==0:
                        tempList.append(l[count][i-1]+l[count][i])
                outputlist.append([l[count][0]+l[count][1],l[count][2]+l[count][3]],tempList)
    return outputlist

def toFEN(ins):
    out=''
    for j in range(8):
        Flag=False
        for i in range(8):
            count=0
            while count+i<8 and ins[j][i+count]=='MT': count+=1
            if ins[j][i][0]=='B':
                out+=ins[j][i][1].lower()
                Flag=False
            elif ins[j][i][0]=='W':
                out+=ins[j][i][1]
                Flag=False
            if count>0:
                i+=(count-1)
                if not Flag:
                    out+=str(count)
                    Flag=True
            if i>=7:
                break
        out+='/'
    return out[0:-1]
