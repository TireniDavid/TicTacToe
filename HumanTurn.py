import time


def human_turn(listChoice, listPosition, HumanPositionCatalog):
    if len(listChoice) > 0:
        User_input_letter_position = input("(Choose either 'X' or 'O') and choose from position(0 to 8): ")
        user_input = list(User_input_letter_position)
        letter_choice = user_input[0].upper()
        position = int(user_input[1])

        while (letter_choice != "X" and letter_choice != "O") or (position < 0 or position > 8):
            print("Invalid")
            User_input_letter_position = input("(Choose either 'X' or 'O') and choose from position(0 to 8): ")
            user_input = list(User_input_letter_position)
            letter_choice = user_input[0].upper()
            position = int(user_input[1])
        playerLetterChoice = listChoice.remove(letter_choice)
        playerPositionChoice = listPosition.remove(position)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        time.sleep(1)
        HumanPositionCatalog.append(position)
        print(f"Human_catalog: {HumanPositionCatalog}")
        time.sleep(1.5)
        HumanPositionCatalog.sort()
        print(f"Human_catalogSORTED:  {HumanPositionCatalog}")
    else:
        position = int(input("(You Chose a letter choice, Now choose from available positions: "))
        playerPositionChoice = listPosition.remove(position)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        HumanPositionCatalog.append(position)
        time.sleep(1)
        print(f"Human_catalog: {HumanPositionCatalog}")
        time.sleep(1.5)
        HumanPositionCatalog.sort()
        print(f"Human_catalogSORTED:  {HumanPositionCatalog}")
        return



