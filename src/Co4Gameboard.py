import numpy as np


class Gameboard:
    def __init__(self, turn): #turn is an int choosing which player goes first
        self.board = np.full((6, 7), -1, dtype=int) #sets the board at its original value
        self.playCount = 0 # to check for stalemate (stalemate is at 6*7=42)
        self.winner = 0 # 0 is no one, 1 is P1, 2 is P2
        self.turn = turn # which player's turn it is

    def takeTurn(self, column):
        return True
        #this one is a simple turn returns false if the column is full
        #true otherwise but checks where to place and checks victory on that particuliar spot

    def checkVictory(self, column,row):
        #from a particuliar spot there's less checks to do
        return True

    def showBoard(self):
        # gotta print more information about the current turn
        print(self.board)