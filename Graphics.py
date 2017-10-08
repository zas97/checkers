import pygame


class Graphics:

    def __init__(self,width,height,board):
        self.board=board
        self.width=width
        self.height=height
        self.widthSquare=int(width/8)
        self.heightSquare=int(height/8)
        #images:
        self.blackPawnPicture = pygame.transform.scale(pygame.image.load("images/PawnBlack.png"),
                                                       (self.widthSquare, self.heightSquare))
        self.blackKingPicture = pygame.transform.scale(pygame.image.load("images/KingBlack.png"),
                                                       (self.widthSquare, self.heightSquare))
        self.whitePawnPicture = pygame.transform.scale(pygame.image.load("images/PawnWhite.png"),
                                                       (self.widthSquare, self.heightSquare))
        self.whiteKingPicture = pygame.transform.scale(pygame.image.load("images/KingWhite.png"),
                                                       (self.widthSquare, self.heightSquare))

        self.drawBoard()


    def drawBoard(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(pygame.Color("black"))

        for i in range(0, 8):
            for j in range(0, 8):
                if (i + j) % 2 == 0:
                    self.drawRectangle((i,j),"white")
        self.drawPieces()
        pygame.display.flip()

    def drawPieces(self):

        for i in range(0,8):
            for j in range(0,8):
                if (i + j) % 2 == 1:
                    if self.board[i][j]==-1:
                        self.drawPiece((i,j),self.blackPawnPicture)
                    elif self.board[i][j]==1:
                        self.drawPiece((i,j),self.whitePawnPicture)
                    elif self.board[i][j]==-3:
                        self.drawPiece((i,j),self.blackKingPicture)
                    elif self.board[i][j]==3:
                        self.drawPiece((i,j),self.whiteKingPicture)



    def getPosition(self,x,y):
        return y*self.widthSquare,x*self.heightSquare

    def getGrid(self,x,y):
        return int(y/self.heightSquare),int(x/self.widthSquare)

    def drawPiece(self,pos,piece):
        self.screen.blit(piece, self.getPosition(pos[0], pos[1]))

    def drawRectangle(self,pos,color,thickness=0):
        pygame.draw.rect(self.screen, pygame.Color(color),
                         pygame.Rect(self.getPosition(pos[0], pos[1])[0],
                                     self.getPosition(pos[0], pos[1])[1], self.widthSquare,
                                     self.heightSquare),thickness)

    def highlight(self,positions):
        for i in positions:
            self.drawRectangle(i,"blue")
        pygame.display.flip()

    def select(self,position):
        self.drawRectangle(position,"blue",thickness=4)
        pygame.display.flip()



    def selectPiece(self,pos):
        self.lastSelect=pos
        self.drawRectangle(pos,"blue",4)
        pygame.display.flip()




