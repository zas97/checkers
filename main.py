from Graphics import*
from Board import*
from Player import*
from Game import*
from Human import*
import time

board = [[0]*8 for i in range(8)]



graph=Graphics(600, 504,board)
b=Board(board,graph)
b2=SimpleBoard(board)
p1=Human(b,graph,True,b2)
p2=Human(b,graph,False,b2)
g=Game(p1,p2,b,graph)




