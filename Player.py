import random
class Player:

    def __init__(self,board,graphics):
        self.board=board


    def getMove(self):
        move=((random.randint(0, 7),random.randint(0, 7)),(random.randint(0, 7),random.randint(0, 7)))
        return move
