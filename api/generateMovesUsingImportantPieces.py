from createBoardLayout import *
import copy
VectorsOfPieces={'Q':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'K':[[[1,0]],[[-1,0]],[[0,1]],[[-0,1]],[[1,1]],[[-1,1]],[[1,-1]],[[-1,-1]]],'B':[[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'R':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],]],'N':[[[2,1]],[[1,2]],[[-2,1]],[[-1,2]],[[2,-1]],[[1,-2]],[[-1,-2]],[[-2,-1]]]}

def removeDuplicates(l):    #looks through a list and removes the duplicate elemets. requres the input list to be sorted
    if len(l)<=1:
        return l
    temp=[]
    flag=True
    for i in range(1,len(l)):
        if flag==True:
            temp.append(l[i-1])
            flag=False
        if not l[i-1]==l[i]:
            flag=True
    if flag==True:
        temp.append(l[len(l)-1])
        flag=False
    return temp

def generateOpponentMoves(boardLayout,importantPieces): #generates squares that the opponent's pieces are threatening
    moves=[]
    for piece in importantPieces:
        if boardLayout[piece[1]][piece[0]][1]=='K':
            continue
        if boardLayout[piece[1]][piece[0]][1]=='P':
            if (boardLayout[piece[1]][piece[0]][0]=='B'):
                moves.append([piece,[piece[0]+1,piece[1]+1]])
                moves.append([piece,[piece[0]-1,piece[1]+1]])
            elif (boardLayout[piece[1]][piece[0]][0]=='W'):
                moves.append([piece,[piece[0]+1,piece[1]-1]])
                moves.append([piece,[piece[0]-1,piece[1]-1]])
        else:
            if not (boardLayout[piece[1]][piece[0]]=='MT'):
                vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
                for direction in vectors:
                    for vector in direction:
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])   
                            if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                                break
    return moves

def enPassantMoves(boardLayout,i,j):    #the moves from en passant
    moves=[]
    if boardLayout[j][i][0]=='W':
        if j==3:
            if i<7 and boardLayout[3][i+1]=='BP':
                startSquare=[i,3]
                positionList=[]
                positionList.append([i+1,3])
                endSquare = [i+1,2]
                moves.append([startSquare,endSquare,positionList])
            if i>0 and boardLayout[3][i-1]=='BP':
                startSquare=[i,3]
                positionList=[]
                positionList.append([i-1,3])
                endSquare = [i-1,2]
                moves.append([startSquare,endSquare,positionList])
    else:
        if j==4:
            if i<7 and boardLayout[4][i+1]=='WP':
                startSquare=[i,4]
                positionList=[]
                positionList.append([i+1,4])
                endSquare = [i+1,5]
                moves.append([startSquare,endSquare,positionList])
            if i>0 and boardLayout[4][i-1]=='WP':
                startSquare=[i,4]
                positionList=[]
                positionList.append([i-1,4])
                endSquare = [i-1,5]
                moves.append([startSquare,endSquare,positionList])
    return moves

def castling(boardLayout,i,j,opponentMoves):    #moves from castling
    l,r=True,True
    moves=[]
    if boardLayout[j][i][0]=='W':
        for piece in opponentMoves:
            if piece[1]==0:
                if i>4:
                    r=False
                elif i<4:
                    l=False
                else:
                    l,r==False,False
            if boardLayout[0][3]!='MT' or boardLayout[0][2]!='MT'or boardLayout[0][1]!='MT':
                l=False
            if boardLayout[0][5]!='MT' or boardLayout[0][6]!='MT':
                r=False
        if l==True:
            moves.append([[4,0],[2,0]])
        if r==True:
            moves.append([[4,0],[6,0]])
    else:
        for piece in opponentMoves:
            if piece[1]==7:
                if i>4:
                    r=False
                elif i<4:
                    l=False
                else:
                    l,r==False,False
            if boardLayout[7][3]!='MT' or boardLayout[7][2]!='MT'or boardLayout[7][1]!='MT':
                l=False
            if boardLayout[7][5]!='MT' or boardLayout[7][6]!='MT':
                r=False
        if l==True:
            moves.append([[4,7],[2,7]])
        if r==True:
            moves.append([[4,7],[6,7]])
    return moves
            
    
def pawnMoves(boardLayout,i,j): #the moves generated from pawns
    moves=[]
    if boardLayout[j][i][0]=='B':
        if i>0 and i<6:
            if j<6:
                if boardLayout[j+1][i]=='MT':
                    moves.append([[i,j],[i,j+1]])
                if boardLayout[j+1][i+1][0]=='W':
                    moves.append([[i,j],[i+1,j+1]])
                if boardLayout[j+1][i-1][0]=='W':
                    moves.append([[i,j],[i-1,j+1]])
            if j==1:
                if boardLayout[2][i]=='MT':
                    if boardLayout[3][i]=='MT':
                        moves.append([[i,j],[i,3]])
    else:
        if i>0 and i<6:
            if j>1:
                if boardLayout[j-1][i]=='MT':
                    moves.append([[i,j],[i,j-1]])
                if boardLayout[j-1][i+1][0]=='B':
                    moves.append([[i,j],[i+1,j-1]])
                if boardLayout[j-1][i-1][0]=='B':
                    moves.append([[i,j],[i-1,j-1]])
            if j==6:
                if boardLayout[5][i]=='MT':
                    if boardLayout[4][i]=='MT':
                        moves.append([[i,j],[i,4]])
    moves=moves+enPassantMoves(boardLayout,i,j)
    return moves

def isCheckAfterMoveingKing(kingposition,layout):   #checks if the king is in check after it has been moved
    if layout[kingposition[1]][kingposition[0]][0]=='B':
        modifier='W'
    else:
        modifier='B'
    if kingposition[0]-1>=0 and kingposition[1]+1<8 and layout[kingposition[1]-1][kingposition[0]-1]=='WP':
        return True
    if kingposition[0]+1<8 and kingposition[1]+1<8 and layout[kingposition[1]-1][kingposition[0]+1]=='WP':
        return True
    vectors=[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9]],[[2,1]],[[1,2]],[[-2,1]],[[-1,2]],[[2,-1]],[[1,-2]],[[-1,-2]],[[-2,-1]]]
    for direction in vectors:
        for vector in direction:
            if vector[1]+kingposition[1]<8 and vector[1]+kingposition[1]>=0 and vector[0]+kingposition[0]<8 and vector[0]+kingposition[0]>=0:
                if (vector[0]==1 or vector[1]==1) and layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]==modifier+'K':
                    return True
                if abs(vector[0])==abs(vector[1]) and (layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]==modifier+'Q' or layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]==modifier+'B'):
                    return True
                elif (vector[0]==0 or vector[1]==0) and (layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]==modifier+'Q' or layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]==modifier+'R'):
                    return True
                elif layout[vector[1]+kingposition[1]][vector[0]+kingposition[0]]==modifier+'N':
                    return True
    return False

def kingMoves(i,j,opponentMoves,boardLayout):
    moves=[]
    vectors=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    for vector in vectors:
        flag=False
        for move in opponentMoves:
            piece=move[1]
            if (((i+vector[0])==piece[0]) and ((j+vector[1])==piece[1])):
                flag=True
        if (i+vector[0])<8 and (i+vector[0])>=0 and (j+vector[1])<8 and (j+vector[1])>=0:
            if boardLayout[j+vector[1]][i+vector[0]][0]==boardLayout[j][i][0] and boardLayout[j+vector[1]][i+vector[0]]!='MT':
                flag=True
        if (i+vector[0])<8 and (i+vector[0])>=0 and (j+vector[1])<8 and (j+vector[1])>=0:
            boardcopy=copy.deepcopy(boardLayout)
            boardcopy[j+vector[1]][i+vector[0]]=boardcopy[j][i]
            boardcopy[j][i]='MT'
            if flag==False and boardLayout[j+vector[1]][i+vector[0]][0]!=boardLayout[j][i][0] and isCheckAfterMoveingKing([i+vector[0],j+vector[1]],boardcopy)==False:
                moves.append([[i,j],[i+vector[0],j+vector[1]]])
    return moves

def isCheckList(i,j,boardLayout,opponentMoves): #generates a list of coordinates that would block a check. the length of the list is 0 when not in check
    if len(opponentMoves)==0:
        return []
    VectorsOfPieces={'Q':[[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[0,0],[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,0],[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[0,0],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[0,0],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[0,0],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9]]],'K':[[[0,0],[1,0]],[[0,0],[-1,0]],[[0,0],[0,1]],[[0,0],[-0,1]],[[0,0],[1,1]],[[0,0],[-1,1]],[[0,0],[1,-1]],[[0,0],[-1,-1]]],'B':[[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]],[[0,0],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9]],[[0,0],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9]],[[0,0],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'R':[[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[0,0],[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,0],[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],]],'N':[[[0,0],[2,1]],[[0,0],[1,2]],[[0,0],[-2,1]],[[0,0],[-1,2]],[[0,0],[2,-1]],[[0,0],[1,-2]],[[0,0],[-1,-2]],[[0,0],[-2,-1]]],'P':[[[0,0],[1,1]],[[0,0],[-1,1]]]}
    squares=[]
    flag=False
    if boardLayout[opponentMoves[0][0][1]][opponentMoves[0][0][0]][0] == 'B':modifier = 1
    else: modifier = -1
    for move in opponentMoves:
        if move[1]==[i,j]:
            vectors=VectorsOfPieces[boardLayout[move[0][1]][move[0][0]][1]]
            for direction in vectors:
                for vector in direction[::-1]:
                    if move[0][0]+modifier*vector[0]<8 and move[0][0]+modifier*vector[0]>=0 and move[0][1]+modifier*vector[1]<8 and move[0][1]+modifier*vector[1]>=0:
                        if [move[0],[move[0][0]+modifier*vector[0],move[0][1]+modifier*vector[1]]] in opponentMoves:
                            flag=True
                        elif flag==True:
                            squares.append([move[0][0]+modifier*vector[0],move[0][1]+modifier*vector[1]])
    return squares
  
def isCheckUsingVectors(kingI,kingJ,pieceI,pieceJ,boardLayout): #uses vectors to check if the king is in check
    vector=[pieceI-kingI,pieceJ-kingJ]
    if vector[0]==vector[1] or vector[0]==-vector[1] or vector[0]==0 or vector[1]==0:
        if vector[0]==0:
            modulus=abs(vector[1])
        else:
            modulus=abs(vector[0])
        unitVector=[vector[0]//modulus,vector[1]//modulus]
        for modulus in range(9):
            if pieceI+modulus*unitVector[0]>=0 and pieceI+modulus*unitVector[0]<8 and pieceJ+modulus*unitVector[1]>=0 and pieceJ+modulus*unitVector[1]<8:
                if not (boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]==boardLayout[pieceJ][pieceJ][0] or boardLayout[pieceJ][pieceJ]=='MT'):
                    if not (boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]=='P' or boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]=='K'):
                        return True
    return False
        
def generateMoves(boardLayout,importantPieces,opponentImportantPieces,pieces,CheckMovesFlag):
    moves=[]
    opponentMoves=generateOpponentMoves(boardLayout,opponentImportantPieces)
    found=False
    if len(importantPieces)>0:
        modifier = boardLayout[importantPieces[0][1]][importantPieces[0][0]][0]
    else:
        if boardLayout[opponentImportantPieces[0][1]][opponentImportantPieces[0][0]][0]=='B':
            modifier = 'W'
        else:
            modifier = 'B'  #when there are no important pieces, then the easy way to find which turn it is can't be used and a convoluted way of finding the turn utilising the opponent moves must be used.
    
    for j in range(8):
        if found==True:
            break
        for i in range(8):
            if boardLayout[j][i]==(modifier + 'K'): #turn used to find the position of the king
                kingPosition=copy.deepcopy([i,j])
                found=True
                break
        else:
            kingPosition=0
    if kingPosition==0:
        return []
    for piece in importantPieces:
        if boardLayout[piece[1]][piece[0]][1]=='P':
            moves=moves+pawnMoves(boardLayout,piece[0],piece[1])
        elif boardLayout[piece[1]][piece[0]][1]=='K':
            moves=moves+kingMoves(piece[0],piece[1],opponentMoves,boardLayout)
        elif boardLayout[piece[1]][piece[0]][1]=='R':
            moves=moves+castling(boardLayout,piece[0],piece[1],opponentMoves)
            vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
            for direction in vectors:
                for vector in direction:
                    if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                        if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                if isCheckUsingVectors(copy.deepcopy(kingPosition)[0],copy.deepcopy(kingPosition)[1],piece[0],piece[1],boardLayout)==False:#find the moves for normal pieces, accounting for castling
                                    moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
                                    break  
                            else:
                                break
                        elif not boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]==boardLayout[piece[1]][piece[0]][0]:
                            moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
        else:
            if not boardLayout[piece[1]][piece[0]]=='MT':
                vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
                for direction in vectors:
                    for vector in direction:
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                                if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                    if isCheckUsingVectors(copy.deepcopy(kingPosition)[0],copy.deepcopy(kingPosition)[1],piece[0],piece[1],boardLayout)==False:#find the moves for normal pieces
                                        moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
                                        break  
                                else:
                                    break
                            else:
                                moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
                           
    if len(moves)<=0 and CheckMovesFlag==False:
        otherPieces=[o for o in pieces if not (o in importantPieces or o in opponentImportantPieces or boardLayout[o[1]][o[0]][0]==boardLayout[opponentImportantPieces[0][1]][opponentImportantPieces[0][0]][0])]   #if the opponent moves yield no moves, try using the rest of the pieces
        if len(otherPieces)>0:
            otherMoves=generateMoves(boardLayout,otherPieces,opponentImportantPieces,pieces,True)
            moves=otherMoves
    
    checkList=isCheckList(copy.deepcopy(kingPosition)[0], copy.deepcopy(kingPosition)[1], copy.deepcopy(boardLayout), opponentMoves)
    if not checkList==[]:#if the king is in check
        checkMoves=[]
        for move in moves:
            if boardLayout[move[0][1]][move[0][0]][1]=='K':
                if not move[1] in checkList:    
                        checkMoves.append(move)
            else:
                if move[1] in checkList:    
                        checkMoves.append(move)
        if len(checkMoves)<=0 and CheckMovesFlag==False:#if the king is and check, but the current important pieces don't have any valid moves
            otherPieces=[o for o in pieces if not (o in importantPieces or o in opponentImportantPieces or boardLayout[o[1]][o[0]][0]==boardLayout[opponentImportantPieces[0][1]][opponentImportantPieces[0][0]][0])]
            if len(otherPieces)>0:
                otherMoves=generateMoves(boardLayout,otherPieces,opponentImportantPieces,pieces,True)
                for move in otherMoves:
                    if boardLayout[move[0][1]][move[0][0]][1]=='K':
                        if not move[1] in checkList:
                            checkMoves.append(move)
                    else:
                        if move[1] in checkList:    
                            checkMoves.append(move)
            else:
                checkmoves=[]
        moves=checkMoves
    moves=sorted(moves)#sorting the moves
    m=removeDuplicates(moves)#remove duplicate moves so they aren't searched through, which would waste time
    return copy.deepcopy(m)

def generateBoardLayout(move,layout):   #generating a board layout from a move
    if len(move)==2:
        layout[move[1][1]][move[1][0]]=layout[move[0][1]][move[0][0]]
        layout[move[0][1]][move[0][0]]='MT'
    elif move[2][0][1]=='B' or move[2][0][1]=='R' or move[2][0][1]=='Q' or move[2][0][1]=='N' :
        layout[move[1][1]][move[1][0]]=move[2][0]
        layout[move[0][1]][move[0][0]]='MT'
    else:
        layout[move[1][1]][move[1][0]]=layout[move[0][1]][move[0][0]]
        layout[move[0][1]][move[0][0]]='MT'
        layout[move[2][0][1]][move[2][0][0]]='MT'
    return layout
            

def generateMovesUsingImportantPieces(boardLayout,importantPieces,opponentImportantPieces,pieces):  #returns only board layout
    moves=generateMoves(boardLayout,importantPieces,opponentImportantPieces,pieces,False)
    outputList,newLayout=[],[]
    if len(moves)>0:
        for move in moves:
            newLayout=generateBoardLayout(move,copy.deepcopy(boardLayout))
            outputList.append(newLayout)
            newLayout=[]
    return outputList

def generatePossibleMovesUsingImportantPieces(boardLayout,importantPieces,opponentImportantPieces,pieces):  #returns both board layout and the move
    moves=generateMoves(boardLayout,importantPieces,opponentImportantPieces,pieces,False)
    outputList,newLayout=[],[]
    if len(moves)>0:
        for move in moves:
            newLayout=generateBoardLayout(move,copy.deepcopy(boardLayout))
            outputList.append([newLayout,move])
            newLayout=[]
    return outputList


if __name__=='__main__':    #used module testing
    import time
    defaultLayout=[
        ['BR','BN','BB','BQ','BK','BB','BN','BR'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['MT','MT','MT','MT','MT','MT','MT','MT'],
        ['WP','WP','WP','WP','WP','WP','WP','WP'],
        ['WR','WN','WB','WQ','WK','WB','WN','WR']]
    print('defaultLayout',toFEN(defaultLayout))
    print('starting in')
    time.sleep(0.25)
    print('3')
    time.sleep(0.25)
    print('2')
    time.sleep(0.25)
    print('1')
    time.sleep(0.25)
    print('go')
    start_time = time.time()
    from findImportantPieces import findImportantPieces
    from translations import*
    wImportantPieces1,bImportantPieces1,pieces=findImportantPieces(defaultLayout)
    print('defaultLayout',toFEN(defaultLayout))
    moves=generateMovesUsingImportantPieces(copy.deepcopy(defaultLayout), bImportantPieces1, wImportantPieces1, pieces)
    time.sleep(0.1)
    print('defaultLayout',toFEN(defaultLayout))
    for move in moves:
        print('             ',toFEN(move))
    print('done')
    print("--- %s seconds ---" % (time.time() - start_time))