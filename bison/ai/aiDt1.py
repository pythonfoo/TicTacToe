import basic
import random


class ai(basic.ai):
    def __init__(self, playerId):
        # init the basic ai class
        super(ai, self).__init__(playerId)

        self.enemyId = 0
        if self.playerId == 1:
            self.enemyId = 2
        else:
            self.enemyId = 1

        self.fieldSize = range(3)
        self.fieldSizeRev = range(2, -1, -1)
        self.countFieldsEnemy = 0
        self.countFieldsPlayer = 0

    def newGame(self):
        self.countFieldsEnemy = 0
        self.countFieldsPlayer = 0

        # def _fieldContainsEnemy(self, fieldContent):

    #	if self.enemyId == fieldContent:
    #		return 1
    #	return 0

    def _fieldContains(self, _id, fieldContent):
        if _id == fieldContent:
            return 1
        return 0

    #def _fieldIsSet(self, fieldContent):
    #	if fieldContent > 0:
    #		return 1
    #	else:
    #		return 0

    def _getSavePosRow(self, row):
        # check if row is ful!
        if row[0] > 0 and row[1] > 0 and row[2] > 0:
            return -1

        ownageEnemyCount = 0
        ownagePlayerCount = 0
        for col in row:
            ownageEnemyCount += self._fieldContains(self.enemyId, col)
            ownagePlayerCount += self._fieldContains(self.playerId, col)

        if ownageEnemyCount == 2 or ownagePlayerCount == 2:
            for col in self.fieldSize:
                if row[col] == 0:
                    return col

        return -1

    def _countFieldUsage(self, gameField):
        self.countFieldsPlayer = 0
        self.countFieldsEnemy = 0
        for row in gameField:
            for cell in row:
                if cell == self.playerId:
                    self.countFieldsPlayer += 1
                elif cell == self.enemyId:
                    self.countFieldsEnemy += 1

    def _getFreePositions(self, gameField):
        freeCoords = []
        for row in self.fieldSize:
            for cell in self.fieldSize:
                if gameField[row][cell] == 0:
                    freeCoords.append([row, cell])
        return freeCoords

    def _getStratPosRow(self, row):
        # check if row is ful!
        if row[0] == 0 and row[1] == 0 and row[2] == 0:
            return []

        ownageEnemyCount = 0
        ownagePlayerCount = 0
        for col in row:
            ownageEnemyCount += self._fieldContains(self.enemyId, col)
            ownagePlayerCount += self._fieldContains(self.playerId, col)

        positions = []
        if ownageEnemyCount == 0 and ownagePlayerCount == 1:
            for col in self.fieldSize:
                if row[col] == 0:
                    positions.append(col)

        return positions

    def _getStrategicPos(self, gameField):
        strategicPositions = []
        #if self.countFieldsPlayer == 0
        #self.countFieldsEnemy = 0
        for row in self.fieldSize:
            tmpPositions = self._getStratPosRow([gameField[row][0], gameField[row][1], gameField[row][2]])
            for pos in tmpPositions:
                strategicPositions.append([row, pos])

            tmpPositions = self._getStratPosRow([gameField[0][row], gameField[1][row], gameField[2][row]])
            for pos in tmpPositions:
                strategicPositions.append([pos, row])

        tmpPositions = self._getStratPosRow([gameField[0][0], gameField[1][1], gameField[2][2]])
        for pos in tmpPositions:
            strategicPositions.append([pos, pos])

        tmpPositions = self._getStratPosRow([gameField[0][2], gameField[1][1], gameField[2][0]])
        for pos in tmpPositions:
            strategicPositions.append([pos, self.fieldSizeRev[pos]])

        return strategicPositions

    def getAiAction(self, gameField):
        #print gameField
        posX = -1
        posY = -1

        haveSavePos = False
        savePosX = -1
        savePosY = -1

        # save pos for row
        if haveSavePos == False:
            for rowX in self.fieldSize:
                savePosY = self._getSavePosRow(gameField[rowX])
                if savePosY != -1:
                    savePosX = rowX
                    haveSavePos = True
                    break

        # save pos for colum
        if haveSavePos == False:
            for colY in self.fieldSize:
                colAr = [gameField[0][colY], gameField[1][colY], gameField[2][colY]]
                savePosX = self._getSavePosRow(colAr)
                if savePosX != -1:
                    savePosY = colY
                    haveSavePos = True
                    break

        # save pos for diag LoRu
        if haveSavePos == False:
            colAr = [gameField[0][0], gameField[1][1], gameField[2][2]]
            savePosY = self._getSavePosRow(colAr)
            if savePosY != -1:
                savePosX = savePosY
                haveSavePos = True

        # save pos for diag RoLu
        if haveSavePos == False:
            colAr = [gameField[0][2], gameField[1][1], gameField[2][0]]
            savePosX = self._getSavePosRow(colAr)
            if savePosX != -1:
                savePosY = self.fieldSizeRev[savePosX]
                haveSavePos = True

        if haveSavePos:
            posX = savePosX
            posY = savePosY
        else:
            self._countFieldUsage(gameField)
            # take the middle in first round or if still empty
            if (self.countFieldsPlayer == 0 and self.countFieldsEnemy == 0) or (
                    (self.countFieldsEnemy + self.countFieldsPlayer) == 1 and gameField[1][1] == 0):
                posX = 1
                posY = 1
            else:
                strategicPos = self._getStrategicPos(gameField)
                if strategicPos != None and strategicPos != []:
                    posX, posY = random.choice(strategicPos)
                else:
                    posX, posY = random.choice(self._getFreePositions(gameField))

        return [posX, posY]


if __name__ == "__main__":
    # check some decisions
    _ai = ai(2)
    gameField = [[1, 0, 0],
                 [0, 2, 0],
                 [0, 1, 0]]
    print 'action:', _ai.getAiAction(gameField)

    # check left-right
    _ai = ai(2)
    gameField = [[2, 0, 0],
                 [0, 0, 0],
                 [1, 1, 0]]
    print 'action:', _ai.getAiAction(gameField)

    # check top-down
    _ai = ai(2)
    gameField = [[2, 1, 0],
                 [0, 1, 0],
                 [0, 0, 0]]
    print 'action:', _ai.getAiAction(gameField)

    # check diag Lo-Ru
    _ai = ai(1)
    gameField = [[2, 1, 0],
                 [0, 2, 0],
                 [1, 0, 0]]
    print 'action:', _ai.getAiAction(gameField)

    # check diag Ro-Lu
    _ai = ai(1)
    gameField = [[0, 1, 2],
                 [0, 2, 0],
                 [0, 0, 1]]
    print 'action:', _ai.getAiAction(gameField)

