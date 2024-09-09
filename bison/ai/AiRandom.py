import ai.Base as basicAi
import random


class Ai(basicAi.Ai):
    def __init__(self, playerId):
        basicAi.Ai.__init__(self, playerId)

    def getAiAction(self, gameField):
        return [random.randint(0, 2), random.randint(0, 2)]