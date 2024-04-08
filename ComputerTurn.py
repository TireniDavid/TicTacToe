import random

def computer_turn(listPosition, ComputerCatalog):
    computerChoice = random.choice(listPosition)
    ComputerCatalog[computerChoice] = True
    return computerChoice

