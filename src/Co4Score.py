import numpy as np


class Score:
    # -*- coding: utf-8 -*-
    """
    A class that represents a scoreboard
    Attributes:
        size (int): The amount of players
        scores (list): The array containing the players' scores
    Methods:
        __init__(self): Initializes the scoreboard
        updateScore(self): Updates the score of a specific player
        getScore(self): returns the score of each player
    """
    def __init__(self, size):
        # -*- coding: utf-8 -*-
        """Builds the Score class

        :param size: the amount of players held in the game
        """
        self.size = size
        self.scores = np.arange(self.size, dtype=int)
        self.scores.fill(0)

    def updateScore(self,player, score):
        # -*- coding: utf-8 -*-
        """ adds a given score to a player's previous score on the scoreboard

        :param player: the player to which the score is to be added
        :param score: the amount of points to add to the scoreboard
        :return: true if the player exists in the scoreboard, false otherwise
        """
        if 0 <= player <= self.size:
            self.scores[player] += score
            return True
        else:
            return False

    def getScore(self):
        # -*- coding: utf-8 -*-
        """ Returns the score of each player

        :return: a string containing the score of each player
        """
        tempMess = "The current score is  : "
        for i in range(len(self.scores)):
            tempMess += "\n Player{} ".format(i)
            tempMess += ":{}  ".format(self.scores[i])
        return tempMess