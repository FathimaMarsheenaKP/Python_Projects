from flask import Flask, render_template, request
import random

app = Flask(__name__)

diceImage = [
    "dice-six-faces-one.png",
    "dice-six-faces-two.png",
    "dice-six-faces-three.png",
    "dice-six-faces-four.png",
    "dice-six-faces-five.png",
    "dice-six-faces-six.png"
]

@app.route('/')
def diceGame():
    return render_template("index.html", dice_img=diceImage[0])

@app.route("/roll", methods=["POST"])
def roll():
    # generate random number
    random_num = random.randint(0, 5)
    return render_template("index.html", dice_img=diceImage[random_num])

if __name__ == '__main__':
    app.run(debug=True)
