###############
import time

import ComputerTurn
import HumanTurn
import WinOrLose

listPosition = [0, 1, 2, 3, 4, 5, 6, 7, 8]
listChoice = ["X", "O"]
letter_choice= 5
HumanPositionCatalog = {0: False, 1: False,
                        2: False, 3: False,
                        4: False, 5: False,
                        6: False, 7: False,
                        8: False}
ComputerPositionCatalog = {0: False, 1: False,
                           2: False, 3: False,
                           4: False, 5: False,
                           6: False, 7: False,
                           8: False}
winPossibilities = {"A": [0, 1, 2],
                    "B": [0, 3, 6],
                    "C": [0, 4, 8],
                    "D": [1, 4, 7],
                    "E": [2, 4, 6],
                    "F": [2, 5, 8],
                    "G": [3, 4, 5],
                    "H": [6, 7, 8]}
#### Start of game

print("Hello Welcome to TicTacToe!!!")
time.sleep(1.5)
print("This is a game between You and the Computer!")
time.sleep(1)
print("Don't worry No winning strategy was implemented for the computer!")
time.sleep(1)
print("Meaning your chances of winning is more than 99%, if your smart")

while len(listPosition) > 0:
    y = HumanTurn.human_turn(listChoice, listPosition, HumanPositionCatalog,letter_choice)
    letter_choice = y
    if WinOrLose.win(HumanPositionCatalog, winPossibilities):
        print('You Won')
        break

    if len(listPosition):
        ComputerTurn.computer_turn(listChoice, listPosition, ComputerPositionCatalog)
        if WinOrLose.win(ComputerPositionCatalog, winPossibilities):
            print('You Lost')
            break
else:
    print('Draw')
print(HumanPositionCatalog)
print(ComputerPositionCatalog)