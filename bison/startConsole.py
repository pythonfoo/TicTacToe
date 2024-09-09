import time
from GameLogic import GameLogic
from InterfaceConsole import InterfaceConsole
from InterfaceAi import InterfaceAi

players = ["placeholder", ]
aiInstances = ["placeholder", None, None]

gl = GameLogic()
gl.start_game()
ic = InterfaceConsole()

players.append(ic.choose_player(1))
players.append(ic.choose_player(2))

for playerId in range(len(players)):
    if players[playerId] == "ai":
        pickedAiId = ic.choose_ai(playerId)
        aiInstances[playerId] = InterfaceAi()
        aiInstances[playerId].init_ai(pickedAiId, playerId)

aiGameRounds = 0
drawGameField = True
if players[1] == "ai" and players[2] == "ai":
    aiGameRounds = ic.choose_ai_game_rounds()
    gl.set_export(aiGameRounds)
    # print game field for every move
    #drawGameField = False

startTime = time.time()
keepPlaying = True
while keepPlaying:
    if gl.is_game_over():

        # tell the AIs what happened
        if players[1] == "ai":
            aiInstances[1].new_game_set_winner(gl.getWinner())

        if players[2] == "ai":
            aiInstances[2].new_game_set_winner(gl.getWinner())

        if aiGameRounds == 0:
            ic.print_stats(gl)
            keepPlaying = ic.play_again()
        elif aiGameRounds > gl.get_played_rounds_count():
            ic.print_progress(gl.get_played_rounds_count(), aiGameRounds)
            keepPlaying = True
        else:
            ic.print_progress(gl.get_played_rounds_count(), aiGameRounds)
            ic.print_stats(gl)
            keepPlaying = False

        if keepPlaying:
            gl.start_game()

    else:
        nextPlayer = gl.get_next_player()

        if drawGameField:
            ic.print_game_field(gl.get_field())
            print("Player", ic.get_player_name(nextPlayer))

        if players[nextPlayer] == "user":
            setWasOk = False
            while not setWasOk:
                setWasOk = gl.set_player(ic.get_user_input())
        else:
            setWasOk = False
            while not setWasOk:
                aiAction = aiInstances[nextPlayer].get_ai_action(gl.get_field())
                setWasOk = gl.set_player(aiAction)

gl.save_export()
print('')
print("playtime:", time.time() - startTime)