defaultLayout=[['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']]
currentLayout=defaultLayout

def staticWeight(boardLayout,specificPiece):    #returns the static weight of pieces
    weights={
        'P':1,
        'N':3,
        'B':3,
        'R':5,
        'Q':9,
        'K':100000
    }
    piece=boardLayout[specificPiece[1]][specificPiece[0]][1]
    return weights[piece]

def enPassantMoves(boardLayout,i,j):    #the pieces being threatened by enapssant
    threatening=[]
    if boardLayout[j][i][0]=='W':
        if j==3:
            if i<7 and boardLayout[3][i+1]=='BP':
                threatening.append([i+1,3])
            if i>0 and boardLayout[3][i-1]=='BP':
                threatening.append([i-1,3])
    else:
        if j==4:
            if i<6 and boardLayout[4][i+1]=='WP':
                threatening.append([i+1,4])
            if i>0 and boardLayout[4][i-1]=='WP':
                threatening.append([i-1,4])
    return threatening

def sort(ins):  #sorting a list using bubble sort
    flag=True
    while flag:
        flag=False
        for i in range(1,len(ins)):
            if ins[i-1][0]>ins[i][0]:
                temp=ins[i-1]
                ins[i-1]=ins[i]
                ins[i]=temp
                falg=True
            elif ins[i-1][0]==ins[i][0]:
                if ins[i-1][1]>ins[i][1]:
                    temp=ins[i-1]
                    ins[i-1]=ins[i]
                    ins[i]=temp
                    falg=True
    return ins

def whatPieceIsThisOneThreatening(boardLayout,SpecificPiecePosition):   #finding what pieces are being threatened recursively using vectors
    VectorsOfPieces={'Q':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],],[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'K':[[[1,0]],[[-1,0]],[[0,1]],[[-0,1]],[[1,1]],[[-1,1]],[[1,-1]],[[-1,-1]]],'B':[[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],],[[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],],[[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[9,-9],],[[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8],[-9,-9],]],'R':[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]],[[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[-9,0]],[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],],[[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],[0,-9],]],'N':[[[2,1]],[[1,2]],[[-2,1]],[[-1,2]],[[2,-1]],[[1,-2]],[[-1,-2]],[[-2,-1]]]}
    threatening=[]
    piece=boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]]
    if piece[1]=='P':   #pawns only
        if piece[0]=='W':
            if SpecificPiecePosition[0]<7 and SpecificPiecePosition[1]>1 and boardLayout[SpecificPiecePosition[1]-1][SpecificPiecePosition[0]+1][0]=='B':
                threatening.append([SpecificPiecePosition[0]+1,SpecificPiecePosition[1]-1])
                if SpecificPiecePosition[1]==1:
                    temp=boardLayout
                    temp[1][SpecificPiecePosition[0]]='MT'  #accounting for promotion
                    temp[0][SpecificPiecePosition[0]]='WQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
            if SpecificPiecePosition[0]>0 and SpecificPiecePosition[1]>1 and boardLayout[SpecificPiecePosition[1]-1][SpecificPiecePosition[0]-1][0]=='B':
                threatening.append([SpecificPiecePosition[0]-1,SpecificPiecePosition[1]-1])
                if SpecificPiecePosition[1]==1:
                    temp=boardLayout
                    temp[1][SpecificPiecePosition[0]]='MT'  #accounting for promotion
                    temp[0][SpecificPiecePosition[0]]='WQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                    temp[0][SpecificPiecePosition[0]]='WN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
            if SpecificPiecePosition[1]==1:
                temp=boardLayout
                temp[1][SpecificPiecePosition[0]]='MT'  #accounting for promotion
                temp[0][SpecificPiecePosition[0]]='WQ'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                temp[0][SpecificPiecePosition[0]]='WR'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                temp[0][SpecificPiecePosition[0]]='WB'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
                temp[0][SpecificPiecePosition[0]]='WN'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],0])
        else:
            if SpecificPiecePosition[0]<7 and SpecificPiecePosition[1]<6 and boardLayout[SpecificPiecePosition[1]+1][SpecificPiecePosition[0]+1][0]=='B':
                threatening.append([SpecificPiecePosition[0]+1,SpecificPiecePosition[1]+1])
                if SpecificPiecePosition[1]==6:
                    temp=boardLayout
                    temp[6][SpecificPiecePosition[0]]='MT'  #accounting for promotion
                    temp[7][SpecificPiecePosition[0]]='BQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
            if SpecificPiecePosition[0]>0 and SpecificPiecePosition[1]<6 and boardLayout[SpecificPiecePosition[1]+1][SpecificPiecePosition[0]-1][0]=='B':
                threatening.append([SpecificPiecePosition[0]-1,SpecificPiecePosition[1]+1])
                if SpecificPiecePosition[1]==6:
                    temp=boardLayout
                    temp[6][SpecificPiecePosition[0]]='MT'  #accounting for promotion
                    temp[7][SpecificPiecePosition[0]]='BQ'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BR'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BB'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                    temp[7][SpecificPiecePosition[0]]='BN'
                    threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
            if SpecificPiecePosition[1]==6:
                temp=boardLayout
                temp[6][SpecificPiecePosition[0]]='MT'
                temp[7][SpecificPiecePosition[0]]='BQ'  #accounting for promotion
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                temp[7][SpecificPiecePosition[0]]='BR'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                temp[7][SpecificPiecePosition[0]]='BB'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                temp[7][SpecificPiecePosition[0]]='BN'
                threatening=threatening+whatPieceIsThisOneThreatening(temp,[SpecificPiecePosition[0],7])
                
        threatening=threatening+enPassantMoves(boardLayout,SpecificPiecePosition[0],SpecificPiecePosition[1])
        if len(threatening)>1:
            threatening,index=sort(threatening),1
            while index<len(threatening):
                if threatening[index-1]==threatening[index]:
                    del threatening[index]
                index+=1
    else:
        moves=VectorsOfPieces[piece[1]] #other pieces
        for direction in moves:
            flag=False
            for vector in direction:
                if SpecificPiecePosition[1]+vector[1]<8 and SpecificPiecePosition[0]+vector[0]<8 and SpecificPiecePosition[1]+vector[1]>=0 and SpecificPiecePosition[0]+vector[0]>=0:
                    if not boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]]=='MT':
                        if boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]]== (boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]][0]+'K'):
                            continue
                        if flag==False:
                            previosCheckedPiece=boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]]
                            threatening.append([SpecificPiecePosition[0]+vector[0],SpecificPiecePosition[1]+vector[1]])
                            flag=True
                        elif (not previosCheckedPiece[0]==piece[0]) and (boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]][1]=='K'or boardLayout[SpecificPiecePosition[1]+vector[1]][SpecificPiecePosition[0]+vector[0]][1]=='Q'):
                            threatening.append([SpecificPiecePosition[0]+vector[0],SpecificPiecePosition[1]+vector[1]])

    if boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]]=='WR' and (SpecificPiecePosition==[0,7] or SpecificPiecePosition==[7,7]) and boardLayout[7][5]=='WK':
        temp=boardLayout
        temp[SpecificPiecePosition[1]][SpecificPiecePosition[0]]='MT'
        if SpecificPiecePosition[0]>5:  #accounting for castling
            temp[7][6]='WR'
            threatening= threatening + whatPieceIsThisOneThreatening(temp, [6,7])
        else:
            temp[7][4]='WR'
            threatening= threatening + whatPieceIsThisOneThreatening(temp, [4,7])
    elif boardLayout[SpecificPiecePosition[1]][SpecificPiecePosition[0]]=='BR' and (SpecificPiecePosition==[0,0] or SpecificPiecePosition==[7,0]) and boardLayout[0][5]=='WK':
        temp=boardLayout
        temp[SpecificPiecePosition[1]][SpecificPiecePosition[0]]='MT'
        if SpecificPiecePosition[0]>5:
            temp[0][6]='BR'  #accounting for castling
            threatening= threatening + whatPieceIsThisOneThreatening(temp, [6,0])
        else:
            temp[0][4]='BR'
            threatening= threatening + whatPieceIsThisOneThreatening(temp, [4,0])

    return threatening


def findWeights(boardLayout,specificPiece,weights):
    if weights[specificPiece[1]][specificPiece[0]]=='MT':
        weightofPiece=staticWeight(boardLayout,specificPiece)
        weights[specificPiece[1]][specificPiece[0]]=weightofPiece
    else:
        weightofPiece=weights[specificPiece[1]][specificPiece[0]]
    threatening=whatPieceIsThisOneThreatening(boardLayout,specificPiece)
    for piece in threatening: #checks if all the pieces have weights
        if len(piece)<2:
            piece=piece[0]
        if weights[piece[1]][piece[0]]=='MT':
            weight=findWeights(boardLayout, piece, weights)
            weightofPiece+=weight[piece[1]][piece[0]]
        else:
            weightofPiece+=weights[piece[1]][piece[0]]
    weights[specificPiece[1]][specificPiece[0]]=weightofPiece
    return weights  #returns a 2d array og all the weights on the board
