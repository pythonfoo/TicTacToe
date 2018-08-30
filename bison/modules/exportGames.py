import numpy as np
import pickle

class exportGames(object):
    def __init__(self):
        self.player1 = np.full((1, 3, 3), -1)
        self.player2 = np.full((1, 3, 3), -1)
        self.winLose = np.full((1, 2), -1)

    def getP1Field(self, x):
        if x == 2:
            return 0
        else:
            return x

    def getP2Field(self, x):
        if x == 1:
            return 0
        elif x == 2:
            return 1
        else:
            return x

    def setWinLose(self, gameIndex, player1, player2):
        self.winLose[gameIndex] = [player1, player2]

    def setPlayField(self, gameIndex, gameField):

        player1_field = [-1, -1, -1]
        player2_field = [-1, -1, -1]

        for i in range(len(gameField)):
            row = gameField[i]
            player1_field[i] = [ self.getP1Field(x) for x in row ]
            player2_field[i] = [ self.getP2Field(x) for x in row ]

            #for y in row:
            #    if y == 1:
            #        pass
        #print player1_field
        #print player2_field
        #print self.winLose[self.gameIndex]

        self.player1[gameIndex] = player1_field
        self.player2[gameIndex] = player2_field

    def setExport(self, amount):
        self.useExport = True
        self.player1 = np.full((amount, 3, 3), -1)
        self.player2 = np.full((amount, 3, 3), -1)
        self.winLose = np.full((amount, 2), -1)
        # [1, 0] player 1 wins
        # [0, 1] player 2 wins
        # [0, 0] draw

    def saveExport(self):
        with open('player1.pkl', 'wb') as f:
            pickle.dump(self.player1, f)
        with open('player2.pkl', 'wb') as f:
            pickle.dump(self.player2, f)
        with open('winLose.pkl', 'wb') as f:
            pickle.dump(self.winLose, f)