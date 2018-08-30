import interfaceAi


class console():
    def __init__(self):
        self.yes = ("yes", "ja", "y", "j", "1", "")
        self.no = ("no", "nein", "n", "0")
        self.printProgressCounter = 0

    def chooseAi(self, playerId):
        validAnswer = False
        ifAi = interfaceAi.interfaceAi()
        while not validAnswer:
            aiList = ifAi.getAiList()
            print("choose AI for", self.getPlayerName(playerId))
            itemCount = 0
            for aiItem in ifAi.getAiList():
                itemCount += 1
                print(str(itemCount) + ") " + aiItem)

            choice = input("choice:")
            if choice.isdigit():
                choiceInt = int(choice) - 1
                if len(aiList) >= choiceInt and choiceInt >= 0:
                    return choiceInt

    def chooseAiGameRounds(self):
        validAnswer = False
        while not validAnswer:
            choice = input("how many rounds should the AI play:")
            if choice.isdigit():
                return int(choice)

    def choosePlayer(self, playerId):
        validAnswer = False
        # ifAi = interfaceAi.interfaceAi()
        while not validAnswer:
            print("Who should player", self.getPlayerName(playerId), "be?")
            print("1) user")
            print("2) CPU")
            choice = input("choice:")
            if choice == "1":
                return "user"
            elif choice == "2":
                return "ai"

    def getPlayerName(self, playerId):
        if playerId == 0:
            return "-"
        elif playerId == 1:
            return "X"
        elif playerId == 2:
            return "O"

    def printGameField(self, gameField):
        finalTable = ""

        # header row / top cords
        finalTable += "  " + " ".join(str(i) for i in range(3)) + "\n"

        rowCount = 0
        for row in gameField:
            # left hand cords
            finalTable += str(rowCount) + " "
            for field in row:
                finalTable += self.getPlayerName(field) + " "

            finalTable += "\n"
            rowCount += 1

        print(finalTable)

    def printStats(self, gl):
        self.printGameField(gl.getField())
        print(13 * "*")
        print("* WINNER:", self.getPlayerName(gl.getWinner()) + " *")
        print(13 * "*")
        print("total games:", gl.getPlayedRoundsCount())
        print("X wins", gl.score[1], "matches")
        print("O wins", gl.score[2], "matches")
        print("draws ", gl.score[0], "matches")

    def printProgress(self, currentGame, maxGame):
        """
        http://www.prozentrechnung.net/
        function prozentrechner2 ()
        {
        x = document.formular2.x.value*100;
        y = x/document.formular2.y.value;
        z = (Math.round(y/0.01)*0.01)
        document.formular2.ergebnis2.value = z
        }
        """
        self.printProgressCounter += 1
        if maxGame < 1000 or self.printProgressCounter >= maxGame / 100 or currentGame == maxGame:
            self.printProgressCounter = 0
            import os

            os.system('clear')
            x = currentGame * 100
            y = x / maxGame
            z = int(y) / 2
            tmpStr = '[' + '{:<50}'.format(int(z) * "#") + ']'
            print(tmpStr)
            formatStr = '{:^' + str(len(tmpStr)) + '}'
            print(formatStr.format(str(currentGame) + ' / ' + str(maxGame)))

    def getUserInput(self):
        cords = []

        while len(cords) != 2:
            cords = []
            choose = input('type XY-coordinates: ')
            for c in choose:
                if c.isdigit():
                    cInt = int(c)
                    # if cInt >= 0 and cInt <= 2:
                    if 0 <= cInt <= 2:
                        cords.append(cInt)
        return cords

    def playAgain(self):
        validAnswer = False
        answer = False
        while not validAnswer:
            yesNo = input('play again? Y/n')

            if yesNo.lower() in self.yes:
                validAnswer = True
                answer = True
            elif yesNo.lower() in self.no:
                validAnswer = True
                answer = False

        return answer