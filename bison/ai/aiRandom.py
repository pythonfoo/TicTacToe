import ai.basic as basicAi
import random


class ai(basicAi.ai):
    def __init__(self, playerId):
        basicAi.ai.__init__(self, playerId)

    def getAiAction(self, gameField):
        return [random.randint(0, 2), random.randint(0, 2)]