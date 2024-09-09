import time
from Gamelogic import Gamelogic
from interfaceConsole import console
from interfaceAi import interfaceAi

players = ["placeholder", ]
aiInstances = ["placeholder", None, None]

gl = Gamelogic()
gl.start_game()
ic = console()

players.append(ic.choosePlayer(1))
players.append(ic.choosePlayer(2))

for playerId in range(len(players)):
    if players[playerId] == "ai":
        pickedAiId = ic.chooseAi(playerId)
        aiInstances[playerId] = interfaceAi()
        aiInstances[playerId].initAi(pickedAiId, playerId)

aiGameRounds = 0
drawGameField = True
if players[1] == "ai" and players[2] == "ai":
    aiGameRounds = ic.chooseAiGameRounds()
    gl.set_export(aiGameRounds)
    # print game field for every move
    #drawGameField = False

startTime = time.time()
keepPlaying = True
while keepPlaying:
    if gl.is_game_over():

        # tell the AIs what happened
        if players[1] == "ai":
            aiInstances[1].newGameSetWinner(gl.getWinner())

        if players[2] == "ai":
            aiInstances[2].newGameSetWinner(gl.getWinner())

        if aiGameRounds == 0:
            ic.printStats(gl)
            keepPlaying = ic.playAgain()
        elif aiGameRounds > gl.get_played_rounds_count():
            ic.printProgress(gl.get_played_rounds_count(), aiGameRounds)
            keepPlaying = True
        else:
            ic.printProgress(gl.get_played_rounds_count(), aiGameRounds)
            ic.printStats(gl)
            keepPlaying = False

        if keepPlaying:
            gl.start_game()

    else:
        nextPlayer = gl.get_next_player()

        if drawGameField:
            ic.printGameField(gl.get_field())
            print("Player", ic.getPlayerName(nextPlayer))

        if players[nextPlayer] == "user":
            setWasOk = False
            while not setWasOk:
                setWasOk = gl.set_player(ic.getUserInput())
        else:
            setWasOk = False
            while not setWasOk:
                aiAction = aiInstances[nextPlayer].getAiAction(gl.get_field())
                setWasOk = gl.set_player(aiAction)

gl.save_export()
print('')
print("playtime:", time.time() - startTime)