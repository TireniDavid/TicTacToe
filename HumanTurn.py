def human_turn(listChoice, listPosition, HumanPositionCatalog):
    if len(listChoice) > 0:
        User_input_letter_position = input("(Choose either 'X' or 'O') and choose from position(0 to 8): ")
        user_input = list(User_input_letter_position)
        letter_choice = user_input[0]
        position = int(user_input[1])

        while (letter_choice != "X" and letter_choice != "O") or (position < 0 or position > 8):
            print("Invalid")
            User_input_letter_position = input("(Choose either 'X' or 'O') and choose from position(0 to 8): ")
            user_input = list(User_input_letter_position)
            letter_choice = user_input[0]
            position = int(user_input[1])
        playerLetterChoice = listChoice.remove(letter_choice)
        playerPositionChoice = listPosition.remove(position)
        print(listPosition)
        HumanPositionCatalog.append(position)

    else:
        position = int(input("(You Chose a letter choice, Now choose from available positions: "))
        playerPositionChoice = listPosition.remove(position)
        print(listPosition)
        HumanPositionCatalog.append(position)
        return



