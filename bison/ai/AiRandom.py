import random
from abc import ABC

import ai.Base as basicAi


class Ai(basicAi.Ai, ABC):
    def __init__(self, player_id):
        super().__init__(player_id)

    def get_ai_action(self, game_field):
        return [random.randint(0, 2), random.randint(0, 2)]
