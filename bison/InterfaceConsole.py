import os

import InterfaceAi


class InterfaceConsole:
    def __init__(self):
        self.yes = ("yes", "ja", "y", "j", "1", "")
        self.no = ("no", "nein", "n", "0")
        self.print_progress_counter = 0

    def choose_ai(self, player_id):
        valid_answer = False
        if_ai = InterfaceAi.InterfaceAi()
        while not valid_answer:
            ai_list = if_ai.get_ai_list()
            print("choose AI for", self.get_player_name(player_id))
            item_count = 0
            for aiItem in if_ai.get_ai_list():
                item_count += 1
                print(str(item_count) + ") " + aiItem)

            choice = input("choice:")
            if choice.isdigit():
                choice_int = int(choice) - 1
                if len(ai_list) >= choice_int and choice_int >= 0:
                    return choice_int

    @staticmethod
    def choose_ai_game_rounds():
        valid_answer = False
        while not valid_answer:
            choice = input("how many rounds should the AI play:")
            if choice.isdigit():
                return int(choice)

    def choose_player(self, player_id):
        valid_answer = False
        # ifAi = InterfaceAi.InterfaceAi()
        while not valid_answer:
            print("Who should player", self.get_player_name(player_id), "be?")
            print("1) user")
            print("2) CPU")
            choice = input("choice:")

            if choice == "1":
                return "user"
            elif choice == "2":
                return "ai"

    @staticmethod
    def get_player_name(player_id):
        if player_id == 0:
            return "-"
        elif player_id == 1:
            return "X"
        elif player_id == 2:
            return "O"

    def print_game_field(self, game_field):
        final_table = ""

        # header row / top cords
        final_table += "  " + " ".join(str(i) for i in range(3)) + "\n"

        row_count = 0
        for row in game_field:
            # left hand cords
            final_table += str(row_count) + " "
            for field in row:
                final_table += self.get_player_name(field) + " "

            final_table += "\n"
            row_count += 1

        print(final_table)

    def print_stats(self, gl):
        self.print_game_field(gl.get_field())
        print(13 * "*")
        print("* WINNER:", self.get_player_name(gl.getWinner()) + " *")
        print(13 * "*")
        print("total games:", gl.get_played_rounds_count())
        print("X wins", gl.score[1], "matches")
        print("O wins", gl.score[2], "matches")
        print("draws ", gl.score[0], "matches")

    def print_progress(self, current_game, max_game):
        """
        https://www.prozentrechnung.net/
        function prozentrechner2 ()
        {
        x = document.formular2.x.value*100;
        y = x/document.formular2.y.value;
        z = (Math.round(y/0.01)*0.01)
        document.formular2.ergebnis2.value = z
        }
        """
        self.print_progress_counter += 1
        if max_game < 1000 or self.print_progress_counter >= max_game / 100 or current_game == max_game:
            self.print_progress_counter = 0

            os.system('clear')

            x = current_game * 100
            y = x / max_game
            z = int(y) / 2
            tmp_str = '[' + '{:<50}'.format(int(z) * "#") + ']'
            print(tmp_str)
            format_str = '{:^' + str(len(tmp_str)) + '}'
            print(format_str.format(str(current_game) + ' / ' + str(max_game)))

    @staticmethod
    def get_user_input():
        cords = []

        while len(cords) != 2:
            cords = []
            choose = input('type XY-coordinates: ')
            for c in choose:
                if c.isdigit():
                    c_int = int(c)
                    # if cInt >= 0 and cInt <= 2:
                    if 0 <= c_int <= 2:
                        cords.append(c_int)

        return cords

    def play_again(self):
        valid_answer = False
        answer = False

        while not valid_answer:
            yes_no = input('play again? Y/n')

            if yes_no.lower() in self.yes:
                valid_answer = True
                answer = True
            elif yes_no.lower() in self.no:
                valid_answer = True
                answer = False

        return answer
