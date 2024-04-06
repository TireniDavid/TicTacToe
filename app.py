import time
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/game")
def game():
    num_cells = 9
    css = ''.join(f""".cell{i} {{
            width: 140px;
            height: 140px;
            justify-content: center;
            align-content: center;
            text-align: center;
        }}
        """ for i in range(1, num_cells + 1))
    return render_template('game.html', num_cells=num_cells, dynamic_css=css)



if __name__ == '__main__':
    app.run(debug=True)

