import time

import ComputerTurn
import HumanTurn
import WinOrLose

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/choice")
def choice():
    return render_template('choice.html')


@app.route("/game", methods=['GET'])
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


@app.route("/update_user_move", methods=['POST'])
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
            return 'You Won', 200
        print(HumanPositionCatalog)

        # remove position from the list
        listPosition.remove(cell_pos)
        print(listPosition)

        return 'User Moved Processed Successfully', 200
    else:
        return 'Method not allowed', 405


@app.route("/send_computer_move", methods=['GET'])
def send_computer_move():
    # computer turn
    # computer to choose randomly from the available slots
    computer_choice = ComputerTurn.computer_turn(listPosition, ComputerPositionCatalog)
    if WinOrLose.win(ComputerPositionCatalog, winPossibilities):
        print('You Lost')

    # reflect computer's choice in the database
    listPosition.remove(computer_choice)
    print(computer_choice)
    print(ComputerPositionCatalog)
    print(f"REMAINING:  {listPosition}")

    # prepare to send computer's data to the front-end
    computer_data = {
        'computerPositionChoice': computer_choice
    }

    # Return Computer's move in JSON format
    return jsonify(computer_data), 200


if __name__ == '__main__':
    app.run(debug=True)
