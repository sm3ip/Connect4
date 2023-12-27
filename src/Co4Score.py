import numpy as np


class Score():
    def __init__(self, size):
        self.size = size
        self.scores = np.arange(self.size, dtype=int)
        self.scores.fill(0)

    def updateScore(self,player, score):
        if 0 <= player <= self.size:
            self.scores[player] += score
            return True
        else:
            return False

    def getScore(self):
        tempMess = "The current score is  : "
        for i in range(len(self.scores)):
            tempMess += "\n Player{} ".format(i)
            tempMess += ":{}  ".format(self.scores[i])
        return tempMess