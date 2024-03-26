winPossibilities = {"A": [0, 1, 2],
                    "B": [0, 3, 6],
                    "C": [0, 4, 8],
                    "D": [1, 4, 7],
                    "E": [2, 4, 6],
                    "F": [2, 5, 8],
                    "G": [3, 4, 5],
                    "H": [6, 7, 8]}
Q
def win(HumanCatalog, ComputerCatalog):
    if len(HumanCatalog) >= 3:
        for value in winPossibilities.values():
            if value in HumanCatalog:
                return "You Win"
            elif value in ComputerCatalog:
                return "You Lose"



