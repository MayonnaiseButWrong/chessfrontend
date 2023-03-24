from createBoardLayout import *
import copy
VectorsOfPieces={'Q':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'K':[[[1,0]],[[-1,0]],[[0,1]],[[-0,1]],[[1,1]],[[-1,1]],[[1,-1]],[[-1,-1]]],'B':[[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'R':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],]],'N':[[[2,1]],[[1,2]],[[-2,1]],[[-1,2]],[[2,-1]],[[1,-2]],[[-1,-2]],[[-2,-1]]]}

def generateOpponentMoves(boardLayout,importantPieces):
    moves=[]
    for piece in importantPieces:
        if boardLayout[piece[1]][piece[0]][1]=='K':
            continue
        if boardLayout[piece[1]][piece[0]][1]=='P':
            if (boardLayout[piece[1]][piece[0]][0]=='W'):
                moves.append([piece,[piece[0]+1,piece[1]+1]])
                moves.append([piece,[piece[0]-1,piece[1]+1]])
            elif (boardLayout[piece[1]][piece[0]][0]=='B'):
                moves.append([piece,[piece[0]+1,piece[1]-1]])
                moves.append([piece,[piece[0]-1,piece[1]-1]])
        else:
            if not (boardLayout[piece[1]][piece[0]]=='MT'):
                vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
                for direction in vectors:
                    for vector in direction:
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                                if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                    moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
                                    break
                                else:
                                    break
                            else:
                                moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
    return moves

def enPassantMoves(boardLayout,i,j):
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

def castling(boardLayout,i,j,opponentMoves):
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
        if l==True:
            moves.append([[4,7],[2,7]])
        if r==True:
            moves.append([[4,7],[6,7]])
    return moves
            
    
def pawnMoves(boardLayout,i,j):
    moves=[]
    if boardLayout[j][i][0]=='B':
        if i>0 and i<7:
            if j<6:
                if boardLayout[j+1][i]=='MT':
                    moves.append([[i,j],[i,j+1]])
                if boardLayout[j+1][i+1][0]=='W':
                    moves.append([[i,j],[i+1,j+1]])
                if boardLayout[j+1][i-1][0]=='W':
                    moves.append([[i,j],[i-1,j+1]])
            if j==1:
                if boardLayout[2][i]=='MT':
                    if boardLayout[3][i]=='MT' or boardLayout[3][i][0]=='W':
                        moves.append([[i,j],[i,3]])
    else:
        if i>0 and i<7:
            if j>1:
                if boardLayout[j-1][i]=='MT':
                    moves.append([[i,j],[i,j-1]])
                if boardLayout[j-1][i+1][0]=='B':
                    moves.append([[i,j],[i+1,j-1]])
                if boardLayout[j-1][i-1][0]=='B':
                    moves.append([[i,j],[i-1,j-1]])
            if j==6:
                if boardLayout[5][i]=='MT':
                    if boardLayout[4][i]=='MT' or boardLayout[4][i][0]=='B':
                        moves.append([[i,j],[i,4]])
    moves=moves+enPassantMoves(boardLayout,i,j)
    return moves

def kingMoves(i,j,opponentMoves):
    moves=[]
    vectors=[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]
    for piece in opponentMoves:
        for vector in vectors:
            if not(((i+vector[0])==piece[0]) and ((j+vector[1])==piece[1])):
                moves.append([[i,j],[i+vector[0],j+vector[1]]])
    return moves

def isCheckList(i,j,boardLayout,opponentMoves):
    squares=[]
    for move in opponentMoves:
        if move[1]==[i,j]:
            vectors=VectorsOfPieces[boardLayout[move[0][1]][move[0][0]]]
            for vector in vectors:
                if [move[0],[move[0][0]+vector[0],move[0][1]+vector[1]]] in opponentMoves:
                    squares.append([move[0][0]+vector[0],move[0][1]+vector[1]])
    return squares
  
def isCheckUsingVectors(kingI,kingJ,pieceI,pieceJ,boardLayout):
    vector=[pieceI-kingI,pieceJ-kingJ]
    if vector[0]==vector[1] or vector[0]==-vector[1] or vector[0]==0 or vector[1]==0:
        if vector[0]==0:
            modulus=abs(vector[1])
        else:
            modulus=abs(vector[0])
        unitVector=[vector[0]//modulus,vector[1]//modulus]
        for modulus in range(9):
            if pieceI+modulus*unitVector[0]>=0 and pieceI+modulus*unitVector[0]<8 and pieceJ+modulus*unitVector[1]>=0 and pieceJ+modulus*unitVector[1]<8:
                if not boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]==boardLayout[pieceJ][pieceJ][0]:
                    if not (boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]=='P' or boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]=='K'):
                        return True
    return False
        
def generateMoves(boardLayout,importantPieces,opponentImportantPieces,pieces):
    moves=[]
    opponentMoves=generateOpponentMoves(boardLayout,opponentImportantPieces)
    found=False
    for j in range(8):
        if found==True:
            break
        for i in range(8):
            if boardLayout[j][i]==(boardLayout[importantPieces[0][1]][importantPieces[0][0]][0] + 'K'):
                kingPosition=[i,j]
                found=True
                break
        else:
            kingPosition = 'did not work'
    print(kingPosition,toFEN(boardLayout))
            
    for piece in importantPieces:
        if boardLayout[piece[1]][piece[0]][1]=='P':
            moves=moves+pawnMoves(boardLayout,piece[0],piece[1])
        elif boardLayout[piece[1]][piece[0]][1]=='K':
            moves=moves+kingMoves(piece[0],piece[1],opponentMoves)
        elif boardLayout[piece[1]][piece[0]][1]=='R':
            moves=moves+castling(boardLayout,piece[0],piece[1],opponentMoves)
            vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
            for direction in vectors:
                for vector in direction:
                    if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                        if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                if isCheckUsingVectors(kingPosition[0],kingPosition[1],piece[0],piece[1],boardLayout)==False:
                                    moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
                                    break
                            else:
                                break
        else:
            if not boardLayout[piece[1]][piece[0]]=='MT':
                vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
                for direction in vectors:
                    for vector in direction:
                        if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
                            if (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
                                if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
                                    if isCheckUsingVectors(kingPosition[0],kingPosition[1],piece[0],piece[1],boardLayout)==False:
                                        moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
                                        break  
                                else:
                                    break
    
    
    checkList=isCheckList(kingPosition[0], kingPosition[1], boardLayout, opponentMoves)
    if not checkList==[]:
        checkMoves=[]
        for move in moves:
            if boardLayout[move[0][0]][move[0][1]][1]=='K':
                if not move[1] in checkList:    
                        checkMoves.append(move)
            else:
                if move[1] in checkList:    
                        checkMoves.append(move)
        if len(checkMoves)==0:
            otherPieces=[o for o in pieces if not (o in importantPieces or o in opponentImportantPieces)]
            otherMoves=generateMoves(boardLayout,otherPieces,opponentImportantPieces)
            for move in otherMoves:
                if boardLayout[move[0][0]][move[0][1]][1]=='K':
                    if not move[1] in checkList:    
                            checkMoves.append(move)
                else:
                    if move[1] in checkList:    
                            checkMoves.append(move)
        moves=checkMoves
    return moves

def generateBoardLayout(move,layout):
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
            

def generateMovesUsingImportantPieces(boardLayout,importantPieces,opponentImportantPieces,pieces):
    moves=generateMoves(boardLayout,importantPieces,opponentImportantPieces,pieces)
    outputList,newLayout=[],[]
    if len(moves)>0:
        for move in moves:
            newLayout=generateBoardLayout(move,copy.deepcopy(boardLayout))
            outputList.append(newLayout)
            newLayout=[]
    return outputList


if __name__=='__main__':
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