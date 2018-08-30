#  0 1 2
#0
#1
#2

import pickle
import numpy as np
import modules.exportGames

class gameLogic():
    def __init__(self):
        self.coord = list(range(3))
        self.reversedCoord = list(range(3))
        self.reversedCoord.reverse()

        self.emptyField = [0, 0, 0]
        self.gameField = []
        self.currentPlayer = 0
        self.gameWinner = -1

        self.score = {0: 0, 1: 0, 2: 0}

        self.useExport = False
        self.exportGames = modules.exportGames.exportGames()
        self.gameIndex = 0

    def setExport(self, amount):
        self.useExport = True
        self.exportGames.setExport(amount)
        # [1, 0] player 1 wins
        # [0, 1] player 2 wins
        # [0, 0] draw

    def saveExport(self):
        if self.useExport:
            self.exportGames.saveExport()
        
    def getPlayedRoundsCount(self):
        return (self.score[0] + self.score[1] + self.score[2])

    def startGame(self):
        newField = []
        for x in self.coord:
            newField.append([0, 0, 0])

        self.gameField = newField
        self.currentPlayer = 0
        self.gameWinner = -1

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getPlayerMulti(self, player):
        if player == 2:
            return 20
        elif player == 1:
            return 1
        else:
            return 0

    def getNextPlayer(self):
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        elif self.currentPlayer == 1:
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1

        return self.currentPlayer

    def getField(self):
        return self.gameField

    def setPlayer(self, cords):
        if self.gameField[cords[0]][cords[1]] != 0:
            return False
        else:
            self.gameField[cords[0]][cords[1]] = self.getCurrentPlayer()
            return True

    def diagonalCheck(self):
        lr = 0
        rl = 0
        for x in self.coord:
            lr += self.getPlayerMulti(self.gameField[x][self.coord[x]])
            rl += self.getPlayerMulti(self.gameField[x][self.reversedCoord[x]])

        return lr, rl

    def isGameOver(self):
        gameOver = False
        horizontals = [0, 0, 0]
        verticals = [0, 0, 0]
        diagonalLR, diagonalRL = self.diagonalCheck()
        lockedFields = 0

        for x in self.coord:
            for y in self.coord:
                addVal = self.getPlayerMulti(self.gameField[x][y])
                if addVal != 0:
                    lockedFields += 1

                horizontals[x] += addVal
                verticals[y] += addVal

                # my math sucks!
                #if x+y == 0 or x+y == 2 or x+y == 4:
                #    diagonalLR += addVal
                #if x+y == 2:
                #    diagonalRL += addVal

        if 3 in horizontals or 3 in verticals or diagonalLR == 3 or diagonalRL == 3:
            gameOver = True
            self.gameWinner = 1
            if self.useExport:
                #self.winLose[self.gameIndex] = [1, 0]
                self.exportGames.setWinLose(self.gameIndex, 1, 0)

        if 60 in horizontals or 60 in verticals or diagonalLR == 60 or diagonalRL == 60:
            gameOver = True
            self.gameWinner = 2
            if self.useExport:
                #self.winLose[self.gameIndex] = [0, 1]
                self.exportGames.setWinLose(self.gameIndex, 0, 1)

        if not gameOver and lockedFields == 9:
            gameOver = True
            self.gameWinner = 0
            if self.useExport:
                #self.winLose[self.gameIndex] = [0, 0]
                self.exportGames.setWinLose(self.gameIndex, 0, 0)

        if gameOver:
            self.score[self.gameWinner] += 1
            '''
            player1_field = [-1, -1, -1]
            player2_field = [-1, -1, -1]
            def getP1Field(x):
                if x == 2:
                    return 0
                else:
                    return x
            def getP2Field(x):
                if x == 1:
                    return 0
                elif x == 2:
                    return 1
                else:
                    return x

            for i in range(len(self.gameField)):
                row = self.gameField[i]
                player1_field[i] = [ getP1Field(x) for x in row ]
                player2_field[i] = [ getP2Field(x) for x in row ]

                for y in row:
                    if y == 1:
                        pass
            #print player1_field
            #print player2_field
            #print self.winLose[self.gameIndex]

            self.player1[self.gameIndex] = player1_field
            self.player2[self.gameIndex] = player2_field'''
            if self.useExport:
                self.exportGames.setPlayField(self.gameIndex, self.gameField)

            self.gameIndex += 1

        return gameOver

    def getWinner(self):
        return self.gameWinner

if __name__ == "__main__":
    gl = gameLogic()
    gl.startGame()
    print(gl.getCurrentPlayer())
    print(gl.getNextPlayer())
    print(gl.getWinner())
    #print gl.getField()

    # BAD for full field check ;)
    #  0 1 2
    #0 X X X
    #1 X O O
    #2 X O O