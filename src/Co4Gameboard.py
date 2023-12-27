import numpy as np


class Gameboard:
    def __init__(self, turn): #turn is an int choosing which player goes first
        self.board = np.full((6, 7), -1, dtype=int) #sets the board at its original value
        self.playCount = 0 # to check for stalemate (stalemate is at 6*7=42)
        self.winner = -1 # -1 is no one, 0 is P1, 1 is P2
        self.turn = turn # which player's turn it is
        self.name = "Connect 4"

    def takeTurn(self, column):
        if column<0 or column>6 or self.board[0][column] != -1:
            return False
        else:
            isDone = False
            for i in range(5,-1,-1):
                if self.board[i][column]==-1 and not isDone:
                    self.board[i][column] = self.turn
                    isDone = True
                    if self.checkVictory(column,i):
                        self.winner = self.turn
            return True
        #this one is a simple turn returns false if the column is full
        #true otherwise but checks where to place and checks victory on that particuliar spot

    def checkVictory(self, column,row):
        #from a particuliar spot there's less checks to do
        tempC = column
        tempR = row
        #gotta check from left to right
        while 1<=tempC<=6 and self.board[tempR][tempC-1]==self.turn:
            tempC-=1 #gets to the furthest left
        streak = 1
        while 0<=tempC<=5 and self.board[tempR][tempC+1]==self.turn:
            streak += 1
            tempC+=1
        if streak>=4:
            return True
        #then check from top to bottom
        while 1<=tempR<=5 and self.board[tempR-1][tempC]==self.turn:
            tempR-=1 #gets to the furthest left
        streak = 1
        while 0<=tempR<=4 and self.board[tempR+1][tempC]==self.turn:
            streak += 1
            tempR+=1
        if streak>=4:
            return True

        #then check from top left to bottom right
        while 1<=tempC<=6 and 1<=tempR<=5 and self.board[tempR-1][tempC-1]==self.turn:
            tempR-=1 #gets to the furthest left
            tempC -= 1
        streak = 1
        while 0<=tempC<=5 and 0<=tempR<=4 and self.board[tempR+1][tempC+1]==self.turn:
            streak += 1
            tempR+=1
            tempC+=1
        if streak>=4:
            return True

        #then check from bottom left to top right

        while 1<=tempC<=6 and 0<=tempR<=4 and self.board[tempR+1][tempC-1]==self.turn:
            tempR+=1 #gets to the furthest left
            tempC -= 1
        streak = 1
        while 0<=tempC<=5 and 1<=tempR<=5 and self.board[tempR-1][tempC+1]==self.turn:
            streak += 1
            tempR-=1
            tempC+=1
        if streak>=4:
            return True

        return False

    def showBoard(self):
        # gotta print more information about the current turn
        print("Next player to play is P", self.turn + 1)
        print("Play count :", self.playCount)
        print(self.board)

    def play(self):
        while self.playCount <43 and self.winner == -1:
            isPlacementGood = False
            while not isPlacementGood:
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