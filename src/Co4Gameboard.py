import numpy as np


class Gameboard:
    # -*- coding: utf-8 -*-
    """
    A class representing a Connect 4 gameBoard
    Attributes:
        board (numpy 2-D array): the gameboard
        playCount (int): the number of turns taken; to check for stalemate (stalemate is at 6*7=42)
        winner (int): the id of this game's winner; -1 is no one, 0 is P1, 1 is P2
        turn (int): the id of this game's turn; 0 is P1, 1 is P2
        name (str): the name of the game
    Methods:
        __init__: initialize the gameBoard
        takeTurn: simulates a turn and returns true if it happened (i.e. if it was possible)
        checkVictory: checks if the previous move landed a victory
        showBoard: prints the gameboard in a pretty format
        play: The game loop
    """
    def __init__(self, turn):
        # -*- coding: utf-8 -*-
        """ Builds the gameBoard

        :param turn: an int deciding on which player goes first
        """
        self.board = np.full((6, 7), -1, dtype=int) #sets the board at its original value
        self.playCount = 0
        self.winner = -1
        self.turn = turn
        self.name = "Connect 4"

    def takeTurn(self, column):
        # -*- coding: utf-8 -*-
        """ Simulates a turn on a given column

        :param column: an int deciding on where the player wants to place their token
        :return: true if the turn was possible, false otherwise
        """
        if column<0 or column>6 or self.board[0][column] != -1:
            return False
        else:
            isDone = False
            for i in range(5,-1,-1):
                #check for the first empty spot in this particuliar column
                if self.board[i][column]==-1 and not isDone:
                    self.board[i][column] = self.turn
                    isDone = True
                    if self.checkVictory(column,i):
                        # when found check if this move was a decisive one
                        self.winner = self.turn
            return True

    def checkVictory(self, column,row):
        # -*- coding: utf-8 -*-
        """ Checks if there are 4 tokens connected to a given spot (the winning condition of this game)

        :param column: an int representing the x-axis of the spot
        :param row: an int representing the y-axis of the spot
        :return: true if the spot is part of a line of 4 tokens (of same value), false otherwise
        """
        tempC = column
        tempR = row
        # Check from left to right
        while 1<=tempC<=6 and self.board[tempR][tempC-1]==self.turn:
            tempC-=1 # gets to the furthest left
        streak = 1
        while 0<=tempC<=5 and self.board[tempR][tempC+1]==self.turn:
            streak += 1 # goes all the way to the right
            tempC+=1
        if streak>=4:
            return True

        # Check from top to bottom
        while 1<=tempR<=5 and self.board[tempR-1][tempC]==self.turn:
            tempR-=1 #gets to the top-most spot with the same token value
        streak = 1
        while 0<=tempR<=4 and self.board[tempR+1][tempC]==self.turn:
            streak += 1 # goes all the way to the bottom
            tempR+=1
        if streak>=4:
            return True

        # Check from top left to bottom right
        while 1<=tempC<=6 and 1<=tempR<=5 and self.board[tempR-1][tempC-1]==self.turn:
            tempR-=1 # gets to the top-left spot with the same token value
            tempC -= 1
        streak = 1
        while 0<=tempC<=5 and 0<=tempR<=4 and self.board[tempR+1][tempC+1]==self.turn:
            streak += 1 # goes all the way to the bottom-right
            tempR+=1
            tempC+=1
        if streak>=4:
            return True

        # Check from bottom left to top right
        while 1<=tempC<=6 and 0<=tempR<=4 and self.board[tempR+1][tempC-1]==self.turn:
            tempR+=1 # gets to the bottom-left spot with the same token value
            tempC -= 1
        streak = 1
        while 0<=tempC<=5 and 1<=tempR<=5 and self.board[tempR-1][tempC+1]==self.turn:
            streak += 1 # goes all the way to the top-right
            tempR-=1
            tempC+=1
        if streak>=4:
            return True

        return False # if no victory condition found

    def showBoard(self):
        # -*- coding: utf-8 -*-
        """
        Displays the board with all the important information
        """
        print("Next player to play is P", self.turn + 1)
        print("Play count :", self.playCount)
        print(self.board)

    def play(self):
        # -*- coding: utf-8 -*-
        """
        Simulates the game loop
        """
        while self.playCount <43 and self.winner == -1:
            isPlacementGood = False
            while not isPlacementGood:
                # take a turn to a given column only if possible
                print("In which column do you wanna play ?")
                column = int(input())
                if self.takeTurn(column):
                    isPlacementGood = True
                else:
                    print("There's no place here try again")
            #turn update
            self.turn = (self.turn+1)%2
            self.playCount += 1
            self.showBoard()
        print("the winner is ", self.winner)