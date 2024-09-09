import pickle
import numpy as np

import modules.exportGames


class Gamelogic:
    def __init__(self):
        self.coord = list(range(3))
        self.reversed_coord = list(range(3))
        self.reversed_coord.reverse()

        self.empty_field = [0, 0, 0]
        self.game_field = []
        self.current_player = 0
        self.game_winner = -1

        self.score = {0: 0, 1: 0, 2: 0}

        self.use_export = False
        self.export_games = modules.exportGames.exportGames()
        self.gameIndex = 0

    def set_export(self, amount):
        self.use_export = True
        self.export_games.setExport(amount)
        # [1, 0] player 1 wins
        # [0, 1] player 2 wins
        # [0, 0] draw

    def save_export(self):
        if self.use_export:
            self.export_games.saveExport()
        
    def get_played_rounds_count(self):
        return self.score[0] + self.score[1] + self.score[2]

    def start_game(self):
        new_field = []
        for x in self.coord:
            new_field.append([0, 0, 0])

        self.game_field = new_field
        self.current_player = 0
        self.game_winner = -1

    def get_current_player(self):
        return self.current_player

    def get_player_multi(self, player):
        if player == 2:
            return 20
        elif player == 1:
            return 1
        else:
            return 0

    def get_next_player(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

        return self.current_player

    def get_field(self):
        return self.game_field

    def set_player(self, cords):
        if self.game_field[cords[0]][cords[1]] != 0:
            return False
        else:
            self.game_field[cords[0]][cords[1]] = self.get_current_player()
            return True

    def diagonal_check(self):
        lr = 0
        rl = 0
        for x in self.coord:
            lr += self.get_player_multi(self.game_field[x][self.coord[x]])
            rl += self.get_player_multi(self.game_field[x][self.reversed_coord[x]])

        return lr, rl

    def is_game_over(self):
        game_over = False
        horizontals = [0, 0, 0]
        verticals = [0, 0, 0]
        diagonal_lr, diagonal_rl = self.diagonal_check()
        locked_fields = 0

        for x in self.coord:
            for y in self.coord:
                add_val = self.get_player_multi(self.game_field[x][y])
                if add_val != 0:
                    locked_fields += 1

                horizontals[x] += add_val
                verticals[y] += add_val

                # my math sucks!
                #if x+y == 0 or x+y == 2 or x+y == 4:
                #    diagonalLR += addVal
                #if x+y == 2:
                #    diagonalRL += addVal

        if 3 in horizontals or 3 in verticals or diagonal_lr == 3 or diagonal_rl == 3:
            game_over = True
            self.game_winner = 1
            if self.use_export:
                #self.winLose[self.gameIndex] = [1, 0]
                self.export_games.setWinLose(self.gameIndex, 1, 0)

        if 60 in horizontals or 60 in verticals or diagonal_lr == 60 or diagonal_rl == 60:
            game_over = True
            self.game_winner = 2
            if self.use_export:
                #self.winLose[self.gameIndex] = [0, 1]
                self.export_games.setWinLose(self.gameIndex, 0, 1)

        if not game_over and locked_fields == 9:
            game_over = True
            self.game_winner = 0
            if self.use_export:
                #self.winLose[self.gameIndex] = [0, 0]
                self.export_games.setWinLose(self.gameIndex, 0, 0)

        if game_over:
            self.score[self.game_winner] += 1
            '''
            player1_field = [-1, -1, -1]
            player2_field = [-1, -1, -1]
            def getP1Field(x):
                if x == 2:
                    return 0
                else:
                    return x
            def getP2Field(x):
                if x == 1:
                    return 0
                elif x == 2:
                    return 1
                else:
                    return x

            for i in range(len(self.game_field)):
                row = self.game_field[i]
                player1_field[i] = [ getP1Field(x) for x in row ]
                player2_field[i] = [ getP2Field(x) for x in row ]

                for y in row:
                    if y == 1:
                        pass
            #print player1_field
            #print player2_field
            #print self.winLose[self.gameIndex]

            self.player1[self.gameIndex] = player1_field
            self.player2[self.gameIndex] = player2_field'''
            if self.use_export:
                self.export_games.setPlayField(self.gameIndex, self.game_field)

            self.gameIndex += 1

        return game_over

    def getWinner(self):
        return self.game_winner


if __name__ == "__main__":
    gl = Gamelogic()
    gl.start_game()
    print(gl.get_current_player())
    print(gl.get_next_player())
    print(gl.getWinner())
    print(gl.get_field())

    # BAD for full field check ;)
    #  0 1 2
    #0 X X X
    #1 X O O
    #2 X O O