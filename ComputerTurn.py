import random
import time

def computer_turn(listChoice, listPosition, ComputerPositionCatalog):
    if len(listChoice) > 0:
        ### list position changes
        ### list choice changes
        computerLetterChoice = (listChoice.pop())
        computerPositionChoice = random.choice(listPosition)
        time.sleep(1)
        print("Computer Choice: " + computerLetterChoice, str(computerPositionChoice))
        listPosition.remove(computerPositionChoice)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        time.sleep(1)
        ComputerPositionCatalog[computerPositionChoice] = True


    else:
        computerPositionChoice = random.choice(listPosition)
        time.sleep(1)
        print("Computer Choice: " + str(computerPositionChoice))
        listPosition.remove(computerPositionChoice)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        time.sleep(1)
        ComputerPositionCatalog[computerPositionChoice] = True
        return

