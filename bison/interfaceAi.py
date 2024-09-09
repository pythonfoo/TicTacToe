import os
import importlib


class interfaceAi():
    def __init__(self):
        self.playerId = 0
        self.aiMap = None
        self.ai = None

    def getAiList(self):
        aiList = []
        for aFile in os.listdir("Ai"):
            if aFile.startswith("Ai") and not "pyc" in aFile:
                aiList.append(aFile.replace(".py", ""))
        return aiList

    def initAi(self, aiId, playerId):
        self.aiMap = importlib.import_module("ai." + self.getAiList()[aiId], "ai")
        self.ai = self.aiMap.Ai(playerId)

        # self.aiMap = __import__("ai." + self.getAiList()[aiId])

    #self.ai = self.aiMap.ai(playerId)

    def getAiAction(self, gameField):
        return self.ai.getAiAction(gameField)

    def newGameSetWinner(self, winner):
        self.ai.setWinner(winner)
        self.ai.newGame()


if __name__ == "__main__":
    import gameLogic

    gl = gameLogic.gameLogic()
    gl.startGame()
    ifAi = interfaceAi()
    print("Ai-list:", ifAi.getAiList())
    ifAi.initAi(int(input("choose ai:")), 1)
    gl.getNextPlayer()
    gl.setPlayer(ifAi.getAiAction(None))
    print(gl.getField())