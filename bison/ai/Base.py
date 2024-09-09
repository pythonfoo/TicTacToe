from abc import abstractmethod


class Ai:
    def __init__(self, player_id):
        self.playerId = player_id

    @abstractmethod
    def get_ai_action(self, game_field):
        pass

    @abstractmethod
    def new_game(self):
        pass

    @abstractmethod
    def set_winner(self, winner_id):
        pass
