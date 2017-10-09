from SimpleBoard import*
import time
import random
class AgentMinimax:

    def __init__(self,board,isWhite,profundity=6):
        self.board=SimpleBoard(board)
        self.white=isWhite
        self.profundity=profundity
        self.iteratorMoves=0
        self.moves=[]

    def negamax(self,profundity,white):
        if profundity==0:
            r=self.board.evalute()
            if white:
                return r
            return -r
        moves=self.board.allMoves(white)
        if len(moves)<=2:
            profundity+=1
        bestMove=None
        m=-40
        for i in moves:
            self.board.play(i)
            aux=-self.negamax(profundity-1,not white)
            if aux>m or (aux==m and bool(random.getrandbits(1))):
                m=aux
                bestMove=i
            self.board.undo()
        self.moves=bestMove
        return m




    def getMove(self):
        self.iteratorMoves+=1
        if self.iteratorMoves>=len(self.moves):
            self.iteratorMoves=0
            print(self.negamax(self.profundity,self.white))
        time.sleep(0.5)
        return self.moves[self.iteratorMoves]



