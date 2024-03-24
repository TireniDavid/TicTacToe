import random

def computer_turn(listChoice, listPosition, ComputerPositionCatalog):
    if len(listChoice) > 0:
        ### list position changes
        ### list choice changes
        computerLetterChoice = listChoice.pop()
        computerPositionChoice = random.choice(listPosition)
        listPosition.remove(computerPositionChoice)
        ComputerPositionCatalog.append(computerPositionChoice)
        print("Computer Choice: " + computerLetterChoice, str(computerPositionChoice))
        print(listPosition)

    else:
        computerPositionChoice = random.choice(listPosition)
        listPosition.remove(computerPositionChoice)
        ComputerPositionCatalog.append(computerPositionChoice)
        print("Computer Choice: " + str(computerPositionChoice))
        print(listPosition)
        return

