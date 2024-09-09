import time

from GameLogic import GameLogic
from InterfaceConsole import InterfaceConsole
from InterfaceAi import InterfaceAi

players = ["placeholder", ]
ai_Instances = ["placeholder", None, None]

gl = GameLogic()
gl.start_game()
ic = InterfaceConsole()

players.append(ic.choose_player(1))
players.append(ic.choose_player(2))

for player_id in range(len(players)):
    if players[player_id] == "ai":
        picked_ai_id = ic.choose_ai(player_id)
        ai_Instances[player_id] = InterfaceAi()
        ai_Instances[player_id].init_ai(picked_ai_id, player_id)

ai_game_rounds = 0
draw_game_field = True
if players[1] == "ai" and players[2] == "ai":
    ai_game_rounds = ic.choose_ai_game_rounds()
    gl.set_export(ai_game_rounds)
    # print game field for every move
    #draw_game_field = False

start_time = time.time()
keep_playing = True
while keep_playing:
    if gl.is_game_over():

        # tell the AIs what happened
        if players[1] == "ai":
            ai_Instances[1].new_game_set_winner(gl.getWinner())

        if players[2] == "ai":
            ai_Instances[2].new_game_set_winner(gl.getWinner())

        if ai_game_rounds == 0:
            ic.print_stats(gl)
            keep_playing = ic.play_again()
        elif ai_game_rounds > gl.get_played_rounds_count():
            ic.print_progress(gl.get_played_rounds_count(), ai_game_rounds)
            keep_playing = True
        else:
            ic.print_progress(gl.get_played_rounds_count(), ai_game_rounds)
            ic.print_stats(gl)
            keep_playing = False

        if keep_playing:
            gl.start_game()

    else:
        next_player = gl.get_next_player()

        if draw_game_field:
            ic.print_game_field(gl.get_field())
            print("Player", ic.get_player_name(next_player))

        if players[next_player] == "user":
            set_was_ok = False
            while not set_was_ok:
                set_was_ok = gl.set_player(ic.get_user_input())
        else:
            set_was_ok = False
            while not set_was_ok:
                ai_action = ai_Instances[next_player].get_ai_action(gl.get_field())
                set_was_ok = gl.set_player(ai_action)

gl.save_export()
print('')
print("playtime:", time.time() - start_time)
