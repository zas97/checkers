import time
import pygame
from sys import exit

class Game:

    def __init__(self,player1,player2,board,graphics):
        self.whites=player1
        self.blacks=player2
        self.board=board
        self.graphics=graphics
        self.start()


    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def start(self):
        whiteTurn=True

        while not self.board.end():
            self.checkQuit()
            if whiteTurn:

                done=False
                while not done:
                    moveFrom, moveTo = self.whites.getMove()
                    if self.board.isWhite(moveFrom):
                        if self.board.playerCanJump(whiteTurn):
                            if moveTo in self.board.posibleJumps(moveFrom):
                                self.board.jump(moveFrom,moveTo)
                                self.chainJumps(moveTo,self.whites)
                                done=True
                        elif moveTo in self.board.posibleMoves(moveFrom):
                            self.board.move(moveFrom,moveTo)
                            done=True

            else:

                done = False
                while not done:
                    moveFrom, moveTo = self.blacks.getMove()
                    if self.board.isBlack(moveFrom):
                        if self.board.playerCanJump(whiteTurn):

                            if moveTo in self.board.posibleJumps(moveFrom):
                                self.board.jump(moveFrom,moveTo)
                                self.chainJumps(moveTo,self.blacks)
                                done=True



                        elif moveTo in self.board.posibleMoves(moveFrom):
                            self.board.move(moveFrom,moveTo)
                            done=True

            self.board.updateBoard();
            
            whiteTurn = not whiteTurn

        print(self.board.end())

    def chainJumps(self,pos,player):
        posibleJumps=self.board.posibleJumps(pos)
        if not posibleJumps==[]:
            correct=False
            while not correct:
                moveFrom,moveTo=player.getMove()
                if moveFrom == pos and moveTo in posibleJumps:
                    self.board.jump(pos,moveTo)
                    correct=True
                    self.chainJumps(moveTo,player)