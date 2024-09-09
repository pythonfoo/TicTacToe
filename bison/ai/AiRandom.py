import random
from abc import ABC

from ai.Base import Ai as AiBase


class Ai(AiBase, ABC):
    def __init__(self, player_id):
        super().__init__(player_id)

    def get_ai_action(self, game_field):
        return [random.randint(0, 2), random.randint(0, 2)]
