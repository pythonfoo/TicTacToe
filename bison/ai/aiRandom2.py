import basic
import random


class ai(basic.ai):
    def __init__(self, playerId):
        # init the basic ai class
        super(ai, self).__init__(playerId)
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