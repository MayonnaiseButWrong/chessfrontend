
def to_xenonnumber(gamelist):
    print('')
    for a in gamelist:
        print(a)
    primeNumbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283.293,307,311,313]
    Pieceslist=['MT','WR','WN','WB','WQ','WK','WP','BR','BN','BB','BQ','BK','BP']
    xenonnumber=1
    n1=0                                                                                              #announcing variables
    n2=0
    n3=0

    for j in range(0,8):                                                                               #there is garunteed to be 36 items in the game list inputted and we need to translate all of them
        for i in range(0,8):
            n1=int(primeNumbers[i+(8*j)])                                                                       #getting the actual numbers needed for the calculation from the list that they're in
            n2=int(Pieceslist.index(gamelist[j][i]))
            n3=n1**n2                                                                                     #the respective prime number to the power of the xenon number for the piece at the corresponding place, multiplied by all the others goves the unique xenon number for the frame
            xenonnumber=xenonnumber*n3

    xenonnumber=str(hex(xenonnumber))
    return xenonnumber

def to_gamelist(ins):
    xenonnumber=int(ins,16)
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
        numcount=0
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
                if not Flag:
                    out+=str(count)
                    Flag=True
            if i>=7:
                break
        out+='/'
    return out[0:-1]

def isInt(ins): #check if a string is an intager
    try:
        int(ins)
    except:
        return False
    else:
        return True

def isBool(ins):    #checking if the string is a boolean, if it is, it returns the value of the boolean, else it returns None
    try:
        ins.lower()
    except:
        return None
    else:
        if ins.lower()=='true':
            return True
        elif ins.lower()=='false':
            return False
        else:
            return None

def formatrequest(ins):#urls don't have spaces, so it replaces them with underscores
    out=''
    for letter in ins:
        if letter==' ':
            out+='_'
        else:
            out+=letter
    return '?fen=' + out + '_b_-_-_0_1'

def formatoutput(ins):  #takes a string as aparameter and returns a dictionary
    ins=ins[1:-1]   #the first and last values of a string are curly braces, and can be ignored
    element,keys,values,lcache,dcache,newdictflag,listflag,lcount,dcount='',[],[],[],'',False,False,0,0 #initialising variables
    for letter in ins:
        if letter=='[': #if a bracket is found, it is the start of a list
            if listflag==False:
                listflag=True
            else:
                lcount+=1#there can be nested lists, thus a count of how many nested lists there are must be kept
        elif letter==']':
            if lcount<=0:#when there are no more nested lists the program end the list and puts it into the next element of the dictionary
                print('here')
                listflag=False
                lcount=0
                element=lcache
        
        if letter=='{':#there can be nested dictionarys, which must be adressed seperately
            if newdictflag==False:
                newdictflag=True
            else:
                dcount+=1#keeping track of how many listed dictionarys there are
        elif letter=='}':
            if dcount<=0:#when there are no nested dictionarys, the program processes them recursivly. the stopping condition is when there is a dictionary with no nested dictionarys
                newdictflag=False
                dcount=0
                element=formatoutput(dcache[1:])   #the first element of the cache is a curly brace, and must be ignored
                dcache=''
            else:
                dcount-=1
        
        if newdictflag==True:   #when a nested dictionary is found, all the elements related to it are kept in a cache to be processed seperately
            dcache+=letter
        elif not (letter=='"' or letter=='{' or letter=='}' or letter=='[' or letter==']' or letter==':' or letter==','):   #excluding the forbidden characters
            element+=letter
            
        if len(element)>0 and element!='':  #when the element is empty,it must be ignored.
            if listflag==True:  #when the current element is part of a list, it is added to the lcache
                if isInt(element)==True:
                    lcache.append(int(element))
                    element=''
                elif isBool(element)!=None:
                    lcache.append(isBool(element))
                    element=''
                else:
                    lcache.append(element)
                    element=''
            elif letter==':':   #if the seperator between elements is a colon, the previos element is a key
                keys.append(element)    #keys are always strings
                element=''
            elif letter==',':   #if the seperator between elements is a comma, the previos element is a value
                if isInt(element)==True:
                    values.append(int(element))
                    element=''
                elif isBool(element)!=None:
                    values.append(isBool(element))
                    element=''
                else:
                    values.append(element)
                    element=''
    values.append(element)  #the last element is always left out by the for loop, and must be added seperately
    resultDictionary = {tuple(keys)[i] : tuple(values)[i] for i, _ in enumerate(tuple(values))} #turning the twp lists into a dictionary using dictoinary comprihension
    return resultDictionary

def fromFENtoBoardLayout(ins):
    print(ins)
    chars=['r','R','b','B','n','N','q','Q','k','K','p','P','1','2','3','4','5','6','7','8']
    ins=ins+' '
    out,direction=[],[]
    for letter in ins:
        if letter==' ':break
        elif letter=='/':
            out.append(direction)
            direction=[]
        if letter in chars:
            if letter == 'r':direction.append('WR')
            elif letter == 'b':direction.append('WB')
            elif letter == 'q':direction.append('WQ')
            elif letter == 'k':direction.append('WK')
            elif letter == 'n':direction.append('WN')
            elif letter == 'p':direction.append('WP')
            elif letter == 'R':direction.append('BR')
            elif letter == 'B':direction.append('BB')
            elif letter == 'Q':direction.append('BQ')
            elif letter == 'K':direction.append('BK')
            elif letter == 'N':direction.append('BN')
            elif letter == 'P':direction.append('BP')
            else: 
                for i in range(int(letter)):
                    direction.append('MT')
    out.append(direction)
    return out[::-1]
        