from createBoardLayout import *
from concurrent.futures import ThreadPoolExecutor
VectorsOfPieces={'Q':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'K':[[[1,0]],[[-1,0]],[[0,1]],[[-0,1]],[[1,1]],[[-1,1]],[[1,-1]],[[-1,-1]]],'B':[[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'R':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],]],'N':[[[2,1]],[[1,2]],[[-2,1]],[[-1,2]],[[2,-1]],[[1,-2]],[[-1,-2]],[[-2,-1]]]}
pool=ThreadPoolExecutor(100)

#def generateOpponentMoves(boardLayout,importantPieces):
#    moves=[]
#    for piece in importantPieces:
#        print(boardLayout[piece[1]][piece[0]][1])
#        if boardLayout[piece[1]][piece[0]][1]=='K':
#            continue
#        if boardLayout[piece[1]][piece[0]][1]=='P':
#            print('here',piece[1],boardLayout[piece[1]][piece[0]][0])
#            if (boardLayout[piece[1]][piece[0]][0]=='W'):
#                moves.append([piece,[piece[0]+1,piece[1]+1]])
#                moves.append([piece,[piece[0]-1,piece[1]+1]])
#                print(moves)
#            elif (boardLayout[piece[1]][piece[0]][0]=='B'):
#                moves.append([piece,[piece[0]+1,piece[1]-1]])
#                moves.append([piece,[piece[0]-1,piece[1]-1]])
#                print(moves)
#        else:
#            vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
#            for direction in vectors:
#                for vector in direction:
#                    if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
#                        if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
#                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
#                                moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
#                                break
#                            else:
#                                break   
#    return moves
#
#def enPassantMoves(boardLayout,i,j):
#    moves=[]
#    if boardLayout[j][i][0]=='W':
#        if j==3:
#            if i<7 and boardLayout[3][i+1]=='BP':
#                startSquare=[i,3]
#                positionList=[]
#                positionList.append([i+1,3])
#                endSquare = [i+1,2]
#                moves.append([startSquare,endSquare,positionList])
#            if i>0 and boardLayout[3][i-1]=='BP':
#                startSquare=[i,3]
#                positionList=[]
#                positionList.append([i-1,3])
#                endSquare = [i-1,2]
#                moves.append([startSquare,endSquare,positionList])
#    else:
#        if j==4:
#            if i<7 and boardLayout[4][i+1]=='WP':
#                startSquare=[i,4]
#                positionList=[]
#                positionList.append([i+1,4])
#                endSquare = [i+1,5]
#                moves.append([startSquare,endSquare,positionList])
#            if i>0 and boardLayout[4][i-1]=='WP':
#                startSquare=[i,4]
#                positionList=[]
#                positionList.append([i-1,4])
#                endSquare = [i-1,5]
#                moves.append([startSquare,endSquare,positionList])
#    return moves
#
#def castling(boardLayout,i,j,opponentMoves):
#    l,r=True,True
#    moves=[]
#    if boardLayout[j][i][0]=='W':
#        for piece in opponentMoves:
#            if piece[1]==0:
#                if i>4:
#                    r=False
#                elif i<4:
#                    l=False
#                else:
#                    l,r==False,False
#        if l==True:
#            moves.append([[4,0],[2,0]])
#        if r==True:
#            moves.append([[4,0],[6,0]])
#    else:
#        for piece in opponentMoves:
#            if piece[1]==7:
#                if i>4:
#                    r=False
#                elif i<4:
#                    l=False
#                else:
#                    l,r==False,False
#        if l==True:
#            moves.append([[4,7],[2,7]])
#        if r==True:
#            moves.append([[4,7],[6,7]])
#    return moves
#            
#    
#def pawnMoves(boardLayout,i,j):
#    moves=[]
#    if boardLayout[j][i][0]=='B':
#        if i>0 and i<7:
#            if j<6:
#                if boardLayout[j+1][i]=='MT':
#                    moves.append([[i,j],[i,j+1]])
#                if boardLayout[j+1][i+1][0]=='W':
#                    moves.append([[i,j],[i+1,j+1]])
#                if boardLayout[j+1][i-1][0]=='W':
#                    moves.append([[i,j],[i-1,j+1]])
#            if j==1:
#                if boardLayout[2][i]=='MT':
#                    if boardLayout[3][i]=='MT' or boardLayout[3][i][0]=='W':
#                        moves.append([[i,j],[i,3]])
#    else:
#        if i>0 and i<7:
#            if j>1:
#                if boardLayout[j-1][i]=='MT':
#                    moves.append([[i,j],[i,j-1]])
#                if boardLayout[j-1][i+1][0]=='B':
#                    moves.append([[i,j],[i+1,j-1]])
#                if boardLayout[j-1][i-1][0]=='B':
#                    moves.append([[i,j],[i-1,j-1]])
#            if j==6:
#                if boardLayout[5][i]=='MT':
#                    if boardLayout[4][i]=='MT' or boardLayout[4][i][0]=='B':
#                        moves.append([[i,j],[i,4]])
#    moves=moves+enPassantMoves(boardLayout,i,j)
#    return moves
#
#def kingMoves(i,j,opponentMoves):
#    moves=[]
#    vectors=[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]
#    for piece in opponentMoves:
#        for vector in vectors:
#            if not(((i+vector[0])==piece[0]) and ((j+vector[1])==piece[1])):
#                moves.append([[i,j],[i+vector[0],j+vector[1]]])
#    return moves
#
#def isCheck(i,j,boardLayout,opponentMoves):
#    for move in opponentMoves:
#        if move[1]==[i,j]:
#            return True
#        else:
#            return False
#
#def isCheckList(i,j,boardLayout,opponentMoves):
#    squares=[]
#    for move in opponentMoves:
#        if move[1]==[i,j]:
#            vectors=VectorsOfPieces[boardLayout[move[0][1]][move[0][0]]]
#            for vector in vectors:
#                if [move[0],[move[0][0]+vector[0],move[0][1]+vector[1]]] in opponentMoves:
#                    squares.append([move[0][0]+vector[0],move[0][1]+vector[1]])
#    return squares
#  
#def isCheckUsingVectors(kingI,kingJ,pieceI,pieceJ,boardLayout):
#    vector=[pieceI-kingI,pieceJ-kingJ]
#    if vector[0]==vector[1] or vector[0]==-vector[1] or vector[0]==0 or vector[1]==0:
#        if vector[0]<0:
#            modulus=-vector[0]
#        elif vector[0]>0:
#            modulus=vector[0]
#        elif vector[1]<0:
#            modulus=-vector[1]
#        else:
#            modulus=vector[1]
#        unitVector=[vector[0]//modulus,vector[1]//modulus]
#        for modulus in range(10):
#            if pieceI+modulus*unitVector[0]>=0 and pieceI+modulus*unitVector[0]<8 and pieceJ+modulus*unitVector[1]>=0 and pieceJ+modulus*unitVector[1]<8:
#                if not boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]==boardLayout[pieceJ][pieceJ]:
#                    if not (boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]=='P' or boardLayout[pieceJ+modulus*unitVector[1]][pieceI+modulus*unitVector[0]][0]=='K'):
#                        return True
#    return False
#        
#def generateMoves(boardLayout,importantPieces,opponentImportantPieces):
#    moves=[]
#    print('boardLayout',boardLayout,'importantPieces',importantPieces,'opponentImportantPieces',opponentImportantPieces)
#    opponentMoves=generateOpponentMoves(boardLayout,opponentImportantPieces)
#    print('opponentMoves',opponentMoves)
#    found=False
#    for j in range(8):
#        if found==True:
#            break
#        for i in range(8):
#            if boardLayout[j][i]==(boardLayout[importantPieces[0][1]][importantPieces[0][0]][0] + 'K'):
#                kingPosition=[i,j]
#                found=True
#                break
#            
#    for piece in importantPieces:
#        if boardLayout[piece[1]][piece[0]][1]=='P':
#            moves=moves+pawnMoves(boardLayout,piece[0],piece[1])
#        elif boardLayout[piece[1]][piece[0]][1]=='K':
#            moves=moves+kingMoves(piece[0],piece[1],opponentMoves)
#        elif boardLayout[piece[1]][piece[0]][1]=='R':
#            moves=moves+castling(boardLayout,piece[0],piece[1],opponentMoves)
#            vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
#            for direction in vectors:
#                for vector in direction:
#                    if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
#                        if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
#                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
#                                if isCheckUsingVectors(kingPosition[0],kingPosition[1],piece[0],piece[1],boardLayout)==False:
#                                    moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
#                                    break
#                            else:
#                                break
#        else:
#            vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]
#            for direction in vectors:
#                for vector in direction:
#                    if (piece[0]+vector[0])>=0 and (piece[0]+vector[0])<8 and (piece[1]+vector[1])>=0 and (piece[1]+vector[1])<8:
#                        if not (boardLayout[piece[1]+vector[1]][piece[0]+vector[0]]=='MT'):
#                            if not (boardLayout[piece[1]][piece[0]][0]==boardLayout[piece[1]+vector[1]][piece[0]+vector[0]][0]):
#                                if isCheckUsingVectors(kingPosition[0],kingPosition[1],piece[0],piece[1],boardLayout)==False:
#                                    moves.append([piece,[piece[0]+vector[0],piece[1]+vector[1]]])
#                                    break  
#                            else:
#                                break
#    
#    
#    checkList=isCheckList(kingPosition[0], kingPosition[1], boardLayout, opponentMoves)
#    if not checkList==[]:
#        checkMoves=[]
#        for move in moves:
#            if boardLayout[move[0][0]][move[0][1]][1]=='K':
#                if not move[1] in checkList:    
#                        checkMoves.append(move)
#            else:
#                if move[1] in checkList:    
#                        checkMoves.append(move)
#        if len(checkMoves)==0:
#            otherPieces=[]
#            for j in range(8):
#                for i in range(8):
#                    if boardLayout[j][i][0]==boardLayout[importantPieces[0][1]][importantPieces[0][0]][0] and not boardLayout[j][i] in importantPieces:
#                        otherPieces.append([i,j])
#            otherMoves=generateMoves(boardLayout,otherPieces,opponentImportantPieces)
#            for move in otherMoves:
#                if boardLayout[move[0][0]][move[0][1]][1]=='K':
#                    if not move[1] in checkList:    
#                            checkMoves.append(move)
#                else:
#                    if move[1] in checkList:    
#                            checkMoves.append(move)
#        moves=checkMoves
#    #print('output',moves)
#    return moves

def normalPieceMoves(layout,x,y,opponentMoves):
    moves=[]
    vectors=VectorsOfPieces[boardLayout[piece[1]][piece[0]][1]]

def generatemoves(boardLayout,importantPieces,opponentImportantPieces):
    moves=[]
    m=[]
    for piece in importantPieces:
        if boardLayout[piece[1]][piece[0]][1]=='P':
            m.append(pool.submit(pawnMoves,boardLayout,piece[0],piece[1]))
        elif boardLayout[piece[1]][piece[0]][1]=='K':
            m.append(pool.submit(kingMovespiece[0],piece[1],opponentMoves))
        elif boardLayout[piece[1]][piece[0]][1]=='R':
            m.append(pool.submit(castling,boardLayout,piece[0],piece[1],opponentMoves))
            m.append(pool.submit(normalPieceMoves,boardLayout,piece[0],piece[1],opponentMoves))
        else:
            m.append(pool.submit(normalPieceMoves,boardLayout,piece[0],piece[1],opponentMoves))
    for a in m:
        move+=a.result()

def generateBoardLayout(move,boardLayout):
    if len(move)==2:
        print(boardLayout[move[1][0]][move[1][1]],boardLayout[move[0][0]][move[0][1]])
        boardLayout[move[1][0]][move[1][1]]=boardLayout[move[0][0]][move[0][1]]
        boardLayout[move[0][0]][move[0][1]]='MT'
        #print(boardLayout[move[1][0]][move[1][1]],boardLayout[move[0][0]][move[0][1]])
    elif move[2][0][1]=='B' or move[2][0][1]=='R' or move[2][0][1]=='Q' or move[2][0][1]=='N' :
        boardLayout[move[1][0]][move[1][1]]=move[2][0]
        boardLayout[move[0][0]][move[0][1]]='MT'
        if len(move[2])>1:
            for pos in range(1,move[2]):
                boardLayout[move[2][pos][1]][move[2][pos][0]]='MT'
    elif len(move[2])>1:
        for pos in range(1,move[2]):
            boardLayout[move[2][pos][1]][move[2][pos][0]]='MT'
    return boardLayout
            

def generateMovesUsingImportantPieces(boardLayout,importantPieces,opponentImportantPieces):
    moves=generateMoves(boardLayout,importantPieces,opponentImportantPieces)
    #
    # for piece in importantPieces:
    #    print(boardLayout[piece[1]][piece[0]])
    #print('here',moves)
    outputList=[]
    if len(moves)>0:
        #outputList=map(generateBoardLayout,moves,boardLayout)
        for move in moves:
            newLayout=generateBoardLayout(move,boardLayout)
            outputList.append(newLayout)
    return outputList
