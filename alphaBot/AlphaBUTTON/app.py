from flask import Flask, render_template, request
from AlphaBot import AlphaBot 
import time

app = Flask(__name__)

bot = AlphaBot()


def move_forward():
    print("Muovendo avanti")
    bot.forward()
    time.sleep(0.5)
    bot.stop()

def move_backward():
    print("Muovendo indietro")
    bot.backward()  
    time.sleep(0.5)
    bot.stop()

def move_left():
    print("Girando a sinistra")
    bot.left()  
    time.sleep(0.5)
    bot.stop()

def move_right():
    print("Girando a destra")
    bot.right()  
    time.sleep(0.5)
    bot.stop()

def stop():
    print("Stop")
    bot.stop()

@app.route("/", methods=["GET", "POST"])
def control():
    if request.method == "POST":
        if "forward" in request.form:
            move_forward()
        elif "backward" in request.form:
            move_backward()
        elif "left" in request.form:
            move_left()
        elif "right" in request.form:
            move_right()
    return render_template("index.html")

@app.route("/shutdown")
def shutdown():
    print("Server arrestato.")
    return "Server arrestato."

if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.125")
