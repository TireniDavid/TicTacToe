import time

def human_turn(listChoice, listPosition, HumanPositionCatalog,letter_choice):
    if len(listChoice) > 0:
        user_input_letter_position = input(
            "You choose either ('X' or 'O') and from position 0 to 8 (comma-separated): ")
        letter_choice = user_input_letter_position.split(',')[0].upper()
        position = int(user_input_letter_position.split(',')[1])
        # if invalid
        while (letter_choice != "X" and letter_choice != "O") or (position < 0 or position > 8):
            user_input_letter_position = input("Invalid Input choose either ('X' or 'O') and from position 0 to 8: ")
            letter_choice = user_input_letter_position.split(',')[0].upper()
            position = int(user_input_letter_position.split(',')[1])
        listChoice.remove(letter_choice)
        listPosition.remove(position)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        HumanPositionCatalog[position] = True
        return letter_choice

    else:
        user_input_letter_position = input(f"Your Letter Choice was: {letter_choice}, Now Choose from position 0 to 8: ")
        position = int(user_input_letter_position)
        ### if invalid
        while position < 0 or position > 8:
            user_input_letter_position = input(f"Invalid Input, Your Letter Choice was: {letter_choice}, Now Choose from position 0 to 8: ")
            position = int(user_input_letter_position)
        listPosition.remove(position)
        time.sleep(1)
        print(f"REMAINING:  {listPosition}")
        HumanPositionCatalog[position] = True
        print(letter_choice)
    return

