###############
import time

import ComputerTurn
import HumanTurn

listPosition = [0, 1, 2, 3, 4, 5, 6, 7, 8]
listChoice = ["X", "O"]
HumanPositionCatalog = []
ComputerPositionCatalog = []

#### Start of game

print("Hello Welcome to TicTacToe")
time.sleep(1.5)
print("This is a game between You and the Computer!")
time.sleep(1)
print("Don't worry No winning strategy was implemented for the computer!")
time.sleep(1)
print("Meaning your chances of winning is 97%")

while len(listPosition) > 0:
    HumanTurn.human_turn(listChoice, listPosition, HumanPositionCatalog)
    time.sleep(1.5)
    if len(listPosition):
        ComputerTurn.computer_turn(listChoice, listPosition, ComputerPositionCatalog)
print(HumanPositionCatalog)
print(ComputerPositionCatalog)