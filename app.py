import time
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/choice")

def choice():
    return render_template('choice.html')
@app.route("/game")
def game():
    return render_template('game.html')



if __name__ == '__main__':
    app.run(debug=True)

