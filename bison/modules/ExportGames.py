import numpy as np
import pickle


class ExportGames(object):
    def __init__(self):
        self.use_export = False

        self.player1 = np.full((1, 3, 3), -1)
        self.player2 = np.full((1, 3, 3), -1)
        self.win_lose = np.full((1, 2), -1)

    @staticmethod
    def get_p1_field(x):
        if x == 2:
            return 0
        else:
            return x

    def get_p2_field(self, x):
        if x == 1:
            return 0
        elif x == 2:
            return 1
        else:
            return x

    def set_win_lose(self, game_index, player1, player2):
        self.win_lose[game_index] = [player1, player2]

    def set_play_field(self, game_index, game_field):

        player1_field = [-1, -1, -1]
        player2_field = [-1, -1, -1]

        for i in range(len(game_field)):
            row = game_field[i]
            player1_field[i] = [self.get_p1_field(x) for x in row]
            player2_field[i] = [self.get_p2_field(x) for x in row]

        self.player1[game_index] = player1_field
        self.player2[game_index] = player2_field

    def set_export(self, amount):
        self.use_export = True
        self.player1 = np.full((amount, 3, 3), -1)
        self.player2 = np.full((amount, 3, 3), -1)
        self.win_lose = np.full((amount, 2), -1)
        # [1, 0] player 1 wins
        # [0, 1] player 2 wins
        # [0, 0] draw

    def save_export(self):
        with open('player1.pkl', 'wb') as f:
            pickle.dump(self.player1, f)
        with open('player2.pkl', 'wb') as f:
            pickle.dump(self.player2, f)
        with open('win_lose.pkl', 'wb') as f:
            pickle.dump(self.win_lose, f)
