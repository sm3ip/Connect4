import Co4Score
import Co4Gameboard
import random

class Co4Game(Co4Score.Score):
    def __init__(self, amountPlayer):
        self.gameBoard = self.chooseGame()
        super().__init__(amountPlayer)

    def chooseGame(self):
        # create a gameboard (we'll be able to choose which one later on)
        return Co4Gameboard.Gameboard(random.randint(0,1))

    def playGame(self):
        doesContinue = 1
        while doesContinue != -1:
            print("Do you wanna play a game of ",self.gameBoard.name ,"? \n (y) yes \n (o) other type of game \n anything else stops it")
            ans = input().lower()
            if ans == 'y':
                self.gameBoard.play()
                if self.gameBoard.winner !=-1:
                    self.updateScore(self.gameBoard.winner,1)
                print(self.getScore())
                self.gameBoard=self.chooseGame()
            else:
                print(self.getScore())
                print("Thank you for playing")
                doesContinue = -1