


import ComputerTurn
import HumanTurn
import WinOrLose

from flask import Flask, render_template, jsonify, request

web_app = Flask(__name__)


@web_app.route("/")
@web_app.route("/home")
def home():
    return render_template('home.html')


@web_app.route("/choice")
def choice():
    return render_template('choice.html')


@web_app.route("/game", methods=['GET'])
def game():
    return render_template('game.html')


winPossibilities = {"A": [0, 1, 2],
                    "B": [0, 3, 6],
                    "C": [0, 4, 8],
                    "D": [1, 4, 7],
                    "E": [2, 4, 6],
                    "F": [2, 5, 8],
                    "G": [3, 4, 5],
                    "H": [6, 7, 8]}
ComputerPositionCatalog = {0: False, 1: False,
                           2: False, 3: False,
                           4: False, 5: False,
                           6: False, 7: False,
                           8: False}
HumanPositionCatalog = {0: False, 1: False,
                        2: False, 3: False,
                        4: False, 5: False,
                        6: False, 7: False,
                        8: False}
listPosition = [0, 1, 2, 3, 4, 5, 6, 7, 8]


@web_app.route("/update_user_move", methods=['POST'])
def update_user_move():
    if request.method == "POST":
        # Get the JSON data
        human_data = request.json
        print("Received data:", human_data)

        cellId = human_data.get("cellName")
        cell_pos = human_data.get("position")
        print(cellId)
        print(cell_pos)

        # human turn
        # change human info database
        HumanTurn.human_turn(cell_pos, HumanPositionCatalog)
        if WinOrLose.win(HumanPositionCatalog, winPossibilities):
            print('You Won')
            Win_Status = {
                'win_status': "You Won"
            }
            return jsonify(Win_Status), 200

        # remove position from the list
        listPosition.remove(cell_pos)
        print(listPosition)

        return 'User Moved Processed Successfully', 200
    else:
        return 'Method not allowed', 405


@web_app.route("/send_computer_move", methods=['GET'])
def send_computer_move():
    # computer turn
    # computer to choose randomly from the available slots
    computer_choice = ComputerTurn.computer_turn(listPosition, ComputerPositionCatalog)

    # reflect computer's choice in the database
    listPosition.remove(computer_choice)
    print(computer_choice)
    print(f"REMAINING:  {listPosition}")

    # prepare to send computer's data to the front-end
    computer_data = {
        'computerPositionChoice': computer_choice
    }
    if WinOrLose.win(ComputerPositionCatalog, winPossibilities):
        computer_data['Win_Status'] = 'You Lost'
        print('You Lost')
    # Return Computer's move in JSON format
    return jsonify(computer_data), 200






if __name__ == '__main__':
    web_app.run(debug=True)
