import time


def human_turn(listChoice, listPosition, HumanPositionCatalog):
    if len(listChoice) > 0:
        User_input_letter_position = input("(Choose either 'X' or 'O') and choose from position(0 to 8): ")
        user_input = User_input_letter_position.split(',')
        letter_choice = user_input[0].upper()
        position = int(user_input[1])

        while (letter_choice != "X" and letter_choice != "O") or (position < 0 or position > 8):
            User_input_letter_position = input("Invalid Input choose either ('X' or 'O') and from position(0 to 8): ")
            user_input = list(User_input_letter_position)
            letter_choice = user_input[0].upper()
            position = int(user_input[1])
        listChoice.remove(letter_choice)
        listPosition.remove(position)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        time.sleep(1.5)
        HumanPositionCatalog[position] = True
    else:
        position = int(input(f"You Chose a letter choice:{letter_choice}, Now choose from the available positions: ")
        while position < 0 or position > 8:
            User_input_letter_position = input("Invalid Input choose from position(0 to 8): ")
            user_input = list(User_input_letter_position)
            letter_choice = user_input[0].upper()
            position = int(user_input[1])
        playerPositionChoice = listPosition.remove(position)
        time.sleep(1)
        print(f"REMAINING: {listPosition}")
        HumanPositionCatalog[position] = True
        return



