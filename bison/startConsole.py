import time
from gameLogic import gameLogic
from interfaceConsole import console
from interfaceAi import interfaceAi

players = ["placeholder", ]
aiInstances = ["placeholder", None, None]

gl = gameLogic()
gl.startGame()
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
    gl.setExport(aiGameRounds)
    # print game field for every move
    #drawGameField = False

startTime = time.time()
keepPlaying = True
while keepPlaying:
    if gl.isGameOver():

        # tell the AIs what happened
        if players[1] == "ai":
            aiInstances[1].newGameSetWinner(gl.getWinner())

        if players[2] == "ai":
            aiInstances[2].newGameSetWinner(gl.getWinner())

        if aiGameRounds == 0:
            ic.printStats(gl)
            keepPlaying = ic.playAgain()
        elif aiGameRounds > gl.getPlayedRoundsCount():
            ic.printProgress(gl.getPlayedRoundsCount(), aiGameRounds)
            keepPlaying = True
        else:
            ic.printProgress(gl.getPlayedRoundsCount(), aiGameRounds)
            ic.printStats(gl)
            keepPlaying = False

        if keepPlaying:
            gl.startGame()

    else:
        nextPlayer = gl.getNextPlayer()

        if drawGameField:
            ic.printGameField(gl.getField())
            print("Player", ic.getPlayerName(nextPlayer))

        if players[nextPlayer] == "user":
            setWasOk = False
            while not setWasOk:
                setWasOk = gl.setPlayer(ic.getUserInput())
        else:
            setWasOk = False
            while not setWasOk:
                aiAction = aiInstances[nextPlayer].getAiAction(gl.getField())
                setWasOk = gl.setPlayer(aiAction)

gl.saveExport()
print('')
print("playtime:", time.time() - startTime)