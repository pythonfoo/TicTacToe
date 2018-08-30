import basic
import random


class ai(basic.ai):
    def getAiAction(self, gameField):
        return [random.randint(0, 2), random.randint(0, 2)]