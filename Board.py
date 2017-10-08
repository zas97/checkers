class Board:

    def __init__(self,board,graphics):
        self.board=board
        self.graphics=graphics
        for i in range(0, 8):
            for j in range(0, 8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        self.board[i][j] = 1
                    elif i >= 5:
                        self.board[i][j] = -1
        graphics.drawBoard()

    def end(self):
        white=True
        black=True
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j]>0:
                    white=False
                elif self.board[i][j]<0:
                    black=False
        return black or white

    def updateBoard(self):
        for i in range(0,8):
            if self.board[0][i]==-1:
                self.board[0][i]=-3
            if self.board[7][i]==1:
                self.board[7][i]=3
        self.graphics.drawBoard();

    def posiblePlaysPiece(self,pos,white):
        posy=pos[0]
        posx=pos[1]
        if white:
            if self.board[posy][posx]>0:
                if self.playerCanJump(True):
                    return self.posibleJumps(pos)
                else:
                    return self.posibleMoves(pos)
        else:
            if self.board[posy][posx]<0:
                if self.playerCanJump(False):
                    return self.posibleJumps(pos)
                else:
                    return self.posibleMoves(pos)
        return []

    def move(self,posFrom,posTo):
        aux=self.board[posFrom[0]][posFrom[1]]
        self.board[posFrom[0]][posFrom[1]]=0
        self.board[posTo[0]][posTo[1]]=aux
        self.graphics.drawBoard()

    def isWhite(self,pos):
        return self.board[pos[0]][pos[1]] > 0

    def isBlack(self,pos):
        return self.board[pos[0]][pos[1]] < 0
    def playerCanJump(self,white):

        if white:
            for i in range(0,8):
                for j in range(0,8):
                    if self.board[i][j]>0:
                        if not self.posibleJumps((i,j))==[]:
                            return True
        else:
            for i in range(0,8):
                for j in range(0,8):
                    if self.board[i][j]<0:
                        if not self.posibleJumps((i,j))==[]:
                            return True
        return False

    def board(self):
        return self.board


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

    def canJump(self,posMid,posTo,piece):
        if piece>0:
            return self.insideBoard(posTo) and self.board[posTo[0]][posTo[1]] == 0 and self.board[posMid[0]][posMid[1]] < 0
        elif piece < 0:
            return self.insideBoard(posTo) and self.board[posTo[0]][posTo[1]] == 0 and self.board[posMid[0]][
                                                                                           posMid[1]] > 0
        return False

    def jump(self,posFrom,posTo):
        aux = self.board[posFrom[0]][posFrom[1]]
        self.board[posFrom[0]][posFrom[1]] = 0
        self.board[int((posFrom[0]+posTo[0])/2)][int((posFrom[1]+posTo[1])/2)] = 0
        self.board[posTo[0]][posTo[1]] = aux
        self.graphics.drawBoard()

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

    def insideBoard(self,pos):
        return pos[0]>=0 and pos[0]<8 and pos[1]>=0 and pos[1]<8