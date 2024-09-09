import random
from abc import ABC

from ai.Base import Ai as AiBase


class Ai(AiBase, ABC):
    def __init__(self, player_id):
        # init the basic Ai class
        super().__init__(player_id)
        self.field_size = range(3)

    def _get_free_positions(self, game_field):
        free_coords = []
        for row in self.field_size:
            for cell in self.field_size:
                if game_field[row][cell] == 0:
                    free_coords.append([row, cell])

        return free_coords

    def get_ai_action(self, game_field):
        return random.choice(self._get_free_positions(game_field))
