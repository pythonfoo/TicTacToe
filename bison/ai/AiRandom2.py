import ai.Base as basicAi
import random


class Ai(basicAi.Ai):
    def __init__(self, playerId):
        # init the basic Ai class
        basicAi.Ai.__init__(self, playerId)
        self.fieldSize = range(3)

    def _getFreePositions(self, gameField):
        freeCoords = []
        for row in self.fieldSize:
            for cell in self.fieldSize:
                if gameField[row][cell] == 0:
                    freeCoords.append([row, cell])
        return freeCoords

    def getAiAction(self, gameField):
        return random.choice(self._getFreePositions(gameField))