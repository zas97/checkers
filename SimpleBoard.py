class SimpleBoard:

    def __init__(self,board):
        self.board=board
        self.buffer=[]
        self.subBuffer = []
        for i in range(0, 8):
            for j in range(0, 8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        self.board[i][j] = 1
                    elif i >= 5:
                        self.board[i][j] = -1


    def evaluate(self):
        r=0
        for i in range(0,8):
            for j in range(0,8):
                r+=self.board[i][j]
        return r

    def assign(self,pos,val,memorize=True):
        if memorize:
            self.subBuffer.append((pos,self.getPiece(pos)))
        self.board[pos[0]][pos[1]]=val

    def getPiece(self,pos):
        return self.board[pos[0]][pos[1]]

    def mid(self,pos1,pos2):
        x=int((pos1[0]+pos2[0])/2)
        y=int((pos1[1]+pos2[1])/2)
        return (x,y)

    def isMove(self,a,b):
        return abs(a[0]-b[0])==1


    def undo(self):
        subBuffer=self.buffer.pop()

        for i in reversed(subBuffer):

            self.assign(i[0],i[1],memorize=False)


    def play(self,moves):
        self.subBuffer = []
        for i in moves:
            moveFrom=i[0]
            moveTo=i[1]
            if self.isMove(moveFrom,moveTo):
                aux=self.getPiece(moveFrom)
                self.assign(moveFrom,0)
                self.assign(moveTo,aux)
            else:
                aux = self.getPiece(moveFrom)
                self.assign(moveFrom, 0)
                self.assign(self.mid(moveFrom,moveTo), 0)
                self.assign(moveTo,aux)
        self.buffer.append(self.subBuffer)



    def generateSequences(self,moves,move,seq):
        print(move)
        self.play(move)
        seq.append(move[0])
        posibleJumps=self.posibleJumps(move[0][1])
        if posibleJumps==[]:
            moves.append(seq)
            self.undo()
            return
        for i in posibleJumps:
            aux=[(move[0][1],i)]
            self.generateSequences(moves,aux,seq)
        self.undo()



    def allMoves(self,white):
        moves=[]
        for i in range(0, 8):
            for j in range(0, 8):
                if (white and self.board[i][j] > 0) or (not white and self.board[i][j] < 0):
                    jump=self.posibleJumps((i,j))
                    for k in jump:
                        aux=[((i,j),(k))]
                        seq=[]
                        self.generateSequences(moves,aux,seq)
        if not moves==[]:
            return moves
        for i in range(0, 8):
            for j in range(0, 8):
                if (white and self.board[i][j] > 0) or (not white and self.board[i][j] < 0):
                    move=self.posibleMoves((i,j))
                    for k in move:
                        moves.append([(((i,j),k))])
        return moves


    def posibleJumps(self,pos):
        posy=pos[0]
        posx=pos[1]
        posibleJumps=[]
        piece = self.board[posy][posx]
        if piece > 0:
            if self.canJump((posy+1,posx+1),(posy+2,posx+2),piece):
                posibleJumps.append((posy+2,posx+2))
            if self.canJump((posy+1,posx-1),(posy+2,posx-2),piece):
                posibleJumps.append((posy+2,posx-2))
            if(piece==3):
                if self.canJump((posy - 1, posx + 1), (posy - 2, posx + 2),piece):
                    posibleJumps.append((posy - 2, posx + 2))
                if self.canJump((posy - 1, posx - 1), (posy - 2, posx - 2),piece):
                    posibleJumps.append((posy - 2, posx - 2))
        if piece < 0:
            if self.canJump((posy - 1, posx + 1), (posy - 2, posx + 2), piece):
                posibleJumps.append((posy - 2, posx + 2))
            if self.canJump((posy - 1, posx - 1), (posy - 2, posx - 2), piece):
                posibleJumps.append((posy - 2, posx - 2))
            if piece==-3:
                if self.canJump((posy + 1, posx + 1), (posy + 2, posx + 2), piece):
                    posibleJumps.append((posy + 2, posx + 2))
                if self.canJump((posy + 1, posx - 1), (posy + 2, posx - 2), piece):
                    posibleJumps.append((posy + 2, posx - 2))



        return posibleJumps

    def canJump(self,posMid,posTo,piece):
        if piece>0:
            return self.insideBoard(posTo) and self.board[posTo[0]][posTo[1]] == 0 and self.board[posMid[0]][posMid[1]] < 0
        elif piece < 0:
            return self.insideBoard(posTo) and self.board[posTo[0]][posTo[1]] == 0 and self.board[posMid[0]][
                                                                                           posMid[1]] > 0
        return False

    def posibleMoves(self,pos):
        posy=pos[0]
        posx=pos[1]
        posibleMoves=[]
        piece=self.board[posy][posx]
        #white or king
        if piece == 1 or abs(piece)==3:
            if self.insideBoard((posy+1,posx+1)) and self.board[posy+1][posx+1]==0:
                posibleMoves.append((posy+1,posx+1))
            if self.insideBoard((posy+1,posx-1)) and self.board[posy + 1][posx - 1] == 0:
                posibleMoves.append((posy + 1, posx - 1))

        if piece == -1 or abs(piece) == 3:
            if self.insideBoard((posy-1,posx+1)) and self.board[posy-1][posx+1]==0:
                posibleMoves.append((posy-1,posx+1))
            if self.insideBoard((posy-1,posx-1)) and self.board[posy - 1][posx - 1] == 0:
                posibleMoves.append((posy - 1, posx - 1))

        return posibleMoves






    def insideBoard(self, pos):
        return pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8
