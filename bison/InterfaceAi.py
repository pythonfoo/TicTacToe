import os
import importlib


class InterfaceAi:
    def __init__(self):
        self.player_id = 0
        self.ai_map = None
        self.ai = None

    @staticmethod
    def get_ai_list():
        ai_list = []
        for ai_file in os.listdir("Ai"):
            if ai_file.startswith("Ai") and "pyc" not in ai_file:
                ai_list.append(ai_file.replace(".py", ""))

        return ai_list

    def init_ai(self, ai_id, player_id):
        self.ai_map = importlib.import_module("ai." + self.get_ai_list()[ai_id], "ai")
        self.ai = self.ai_map.Ai(player_id)

    def get_ai_action(self, game_field):
        return self.ai.get_ai_action(game_field)

    def new_game_set_winner(self, winner):
        self.ai.set_winner(winner)
        self.ai.new_game()


if __name__ == "__main__":
    import GameLogic

    gl = GameLogic.GameLogic()
    gl.start_game()
    ifAi = InterfaceAi()
    print("Ai-list:", ifAi.get_ai_list())
    ifAi.init_ai(int(input("choose ai:")), 1)
    gl.get_next_player()
    gl.set_player(ifAi.get_ai_action(None))
    print(gl.get_field())
