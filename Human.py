import pygame
from SimpleBoard import*
from sys import exit

class Human:

    def __init__(self,board,graphics,isWhite):
        self.graphics=graphics
        self.board=board
        self.isWhite=isWhite


    def getMove(self):
        done=False
        moveFrom=None
        moveTo=None
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if pygame.mouse.get_pressed()[0]:
                (x, y) = pygame.mouse.get_pos()
                (x, y) = self.graphics.getGrid(x,y)
                if moveFrom==None:
                    moveFrom=(x, y)
                    self.graphics.selectPiece(moveFrom)
                    self.graphics.highlight(self.board.posiblePlaysPiece(moveFrom,self.isWhite))
                else:
                    if (x,y) in self.board.posiblePlaysPiece(moveFrom,self.isWhite):
                        moveTo=(x,y)
                        done=True
                    else:
                        self.graphics.drawBoard()
                        moveFrom=(x,y)
                        self.graphics.selectPiece(moveFrom)
                        self.graphics.highlight(self.board.posiblePlaysPiece(moveFrom, self.isWhite))
        return (moveFrom,moveTo)






