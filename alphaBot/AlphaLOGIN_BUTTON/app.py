from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from AlphaBot import AlphaBot  # Importa il modulo per controllare il bot
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Percorso al database SQLite
DATABASE = 'login_db.db'

# Istanza di AlphaBot
bot = AlphaBot()

# Funzioni di movimento del bot
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


# Rotta per la pagina di login
@app.route('/')
def home():
    return render_template('login.html')



# Rotta per la gestione del login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['e-mail']
    password = request.form['password']

    # Connessione al database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        flash('Login successful!', 'success')
        return redirect(url_for('control'))  # Reindirizza alla pagina di controllo del bot
    else:
        print("Login failed!")
        flash('Invalid username or password!', 'danger')
        return redirect(url_for('home'))


# Rotta per controllare il bot
@app.route('/control', methods=["GET", "POST"])
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
        elif "stop" in request.form:
            stop()
    return render_template("index.html")  # Pagina per controllare il bot


# Rotta per spegnere il server (opzionale)
@app.route("/shutdown")
def shutdown():
    print("Server arrestato.")
    return "Server arrestato."


if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.125")
