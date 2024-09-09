import random
from abc import ABC

import ai.Base as basicAi


class Ai(basicAi.Ai, ABC):
    def __init__(self, player_id):
        # init the basic Ai class
        super().__init__(player_id)

        self.enemy_id = 0
        if self.playerId == 1:
            self.enemy_id = 2
        else:
            self.enemy_id = 1

        self.field_size = range(3)
        self.field_size_rev = range(2, -1, -1)
        self.count_fields_enemy = 0
        self.count_fields_player = 0

    def new_game(self):
        self.count_fields_enemy = 0
        self.count_fields_player = 0

        # def _fieldContainsEnemy(self, field_content):

    #	if self.enemy_id == field_content:
    #		return 1
    #	return 0

    def _field_contains(self, _id, field_content):
        if _id == field_content:
            return 1

        return 0

    #def _fieldIsSet(self, field_content):
    #	if field_content > 0:
    #		return 1
    #	else:
    #		return 0

    def _get_save_pos_row(self, row):
        # check if row is ful!
        if row[0] > 0 and row[1] > 0 and row[2] > 0:
            return -1

        ownage_enemy_count = 0
        ownage_player_count = 0
        for col in row:
            ownage_enemy_count += self._field_contains(self.enemy_id, col)
            ownage_player_count += self._field_contains(self.playerId, col)

        if ownage_enemy_count == 2 or ownage_player_count == 2:
            for col in self.field_size:
                if row[col] == 0:
                    return col

        return -1

    def _count_field_usage(self, game_field):
        self.count_fields_player = 0
        self.count_fields_enemy = 0
        for row in game_field:
            for cell in row:
                if cell == self.playerId:
                    self.count_fields_player += 1
                elif cell == self.enemy_id:
                    self.count_fields_enemy += 1

    def _get_free_positions(self, game_field):
        free_coords = []
        for row in self.field_size:
            for cell in self.field_size:
                if game_field[row][cell] == 0:
                    free_coords.append([row, cell])
        return free_coords

    def _get_strat_pos_row(self, row):
        # check if row is ful!
        if row[0] == 0 and row[1] == 0 and row[2] == 0:
            return []

        ownage_enemy_count = 0
        ownage_player_count = 0
        for col in row:
            ownage_enemy_count += self._field_contains(self.enemy_id, col)
            ownage_player_count += self._field_contains(self.playerId, col)

        positions = []
        if ownage_enemy_count == 0 and ownage_player_count == 1:
            for col in self.field_size:
                if row[col] == 0:
                    positions.append(col)

        return positions

    def _get_strategic_pos(self, game_field):
        strategic_positions = []
        #if self.count_fields_player == 0
        #self.count_fields_enemy = 0
        for row in self.field_size:
            tmp_positions = self._get_strat_pos_row([game_field[row][0], game_field[row][1], game_field[row][2]])
            for pos in tmp_positions:
                strategic_positions.append([row, pos])

            tmp_positions = self._get_strat_pos_row([game_field[0][row], game_field[1][row], game_field[2][row]])
            for pos in tmp_positions:
                strategic_positions.append([pos, row])

        tmp_positions = self._get_strat_pos_row([game_field[0][0], game_field[1][1], game_field[2][2]])
        for pos in tmp_positions:
            strategic_positions.append([pos, pos])

        tmp_positions = self._get_strat_pos_row([game_field[0][2], game_field[1][1], game_field[2][0]])
        for pos in tmp_positions:
            strategic_positions.append([pos, self.field_size_rev[pos]])

        return strategic_positions

    def get_ai_action(self, game_field):
        #print game_field
        pos_x = -1
        pos_y = -1

        have_save_position = False
        save_position_x = -1
        save_position_y = -1

        # save pos for row
        if have_save_position == False:
            for rowX in self.field_size:
                save_position_y = self._get_save_pos_row(game_field[rowX])
                if save_position_y != -1:
                    save_position_x = rowX
                    have_save_position = True
                    break

        # save pos for colum
        if have_save_position == False:
            for col_y in self.field_size:
                col_ar = [game_field[0][col_y], game_field[1][col_y], game_field[2][col_y]]
                save_position_x = self._get_save_pos_row(col_ar)
                if save_position_x != -1:
                    save_position_y = col_y
                    have_save_position = True
                    break

        # save pos for diag LoRu
        if have_save_position == False:
            col_ar = [game_field[0][0], game_field[1][1], game_field[2][2]]
            save_position_y = self._get_save_pos_row(col_ar)
            if save_position_y != -1:
                save_position_x = save_position_y
                have_save_position = True

        # save pos for diag RoLu
        if have_save_position == False:
            col_ar = [game_field[0][2], game_field[1][1], game_field[2][0]]
            save_position_x = self._get_save_pos_row(col_ar)
            if save_position_x != -1:
                save_position_y = self.field_size_rev[save_position_x]
                have_save_position = True

        if have_save_position:
            pos_x = save_position_x
            pos_y = save_position_y
        else:
            self._count_field_usage(game_field)
            # take the middle in first round or if still empty
            if (self.count_fields_player == 0 and self.count_fields_enemy == 0) or (
                    (self.count_fields_enemy + self.count_fields_player) == 1 and game_field[1][1] == 0):
                pos_x = 1
                pos_y = 1
            else:
                strategic_pos = self._get_strategic_pos(game_field)
                if strategic_pos != None and strategic_pos != []:
                    pos_x, pos_y = random.choice(strategic_pos)
                else:
                    pos_x, pos_y = random.choice(self._get_free_positions(game_field))

        return [pos_x, pos_y]


if __name__ == "__main__":
    # check some decisions
    _ai = Ai(2)
    gameField = [[1, 0, 0],
                 [0, 2, 0],
                 [0, 1, 0]]
    print('action:', _ai.get_ai_action(gameField))

    # check left-right
    _ai = Ai(2)
    gameField = [[2, 0, 0],
                 [0, 0, 0],
                 [1, 1, 0]]
    print('action:', _ai.get_ai_action(gameField))

    # check top-down
    _ai = Ai(2)
    gameField = [[2, 1, 0],
                 [0, 1, 0],
                 [0, 0, 0]]
    print('action:', _ai.get_ai_action(gameField))

    # check diag Lo-Ru
    _ai = Ai(1)
    gameField = [[2, 1, 0],
                 [0, 2, 0],
                 [1, 0, 0]]
    print('action:', _ai.get_ai_action(gameField))

    # check diag Ro-Lu
    _ai = Ai(1)
    gameField = [[0, 1, 2],
                 [0, 2, 0],
                 [0, 0, 1]]
    print('action:', _ai.get_ai_action(gameField))
