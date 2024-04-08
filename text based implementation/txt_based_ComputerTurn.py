import random
import time

def computer_turn(listChoice, listPosition, ComputerPositionCatalog):
    if len(listChoice) > 0:
        computerLetterChoice = (listChoice.pop())
    computerPositionChoice = random.choice(listPosition)
    print("Computer Choice: " + str(computerPositionChoice))
    listPosition.remove(computerPositionChoice)
    print(f"REMAINING:  {listPosition}")
    time.sleep(1)
    ComputerPositionCatalog[computerPositionChoice] = True
    return

