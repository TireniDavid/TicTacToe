def win(PositionCatalog, winPossibilities):
        count = 0
        for winCombination in winPossibilities.values():
            count = 0
            if count < 3:
                for position in winCombination:
                    if PositionCatalog[position] != True:
                        break
                    elif count == 2:
                        count += 1
                        return True
                    else:
                        count += 1
        else:
            return False





