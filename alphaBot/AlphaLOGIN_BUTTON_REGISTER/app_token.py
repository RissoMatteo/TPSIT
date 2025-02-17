from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import sqlite3
import time
import jwt
import datetime
from functools import wraps
from AlphaBot import AlphaBot 

app = Flask(__name__)
app.secret_key = 'your_secret_key'
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

# Decoratore per proteggere le rotte con JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            flash('Token is missing! Please log in.', 'warning')
            return redirect(url_for('home'))
        try:
            jwt.decode(token, app.secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            flash('Token expired! Please log in again.', 'danger')
            return redirect(url_for('home'))
        except jwt.InvalidTokenError:
            flash('Invalid token!', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated

# Rotta per la pagina di login
@app.route('/')
def home():
    return render_template('login.html')

# Rotta per la gestione del login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['e-mail']
    password = request.form['password']

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 
                           app.secret_key, algorithm='HS256')
        response = make_response(redirect(url_for('control')))
        response.set_cookie('token', token, httponly=True, secure=True)
        return response
    else:
        flash('Invalid username or password!', 'danger')
        return redirect(url_for('home'))

# Rotta per controllare il bot
@app.route('/control', methods=["GET", "POST"])
@token_required
def control():
    token = request.cookies.get('token')
    decoded = jwt.decode(token, app.secret_key, algorithms=['HS256'])
    user = decoded['user']

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
    return render_template("index.html", user=user)

# Rotta per la pagina di registrazione
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['e-mail']
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('User already exists!', 'danger')
            conn.close()
            return redirect(url_for('register'))

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html')

# Rotta per il logout
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('home')))
    response.delete_cookie('token')
    flash('You have been logged out.', 'success')
    return response

# Rotta per spegnere il server (opzionale)
@app.route("/shutdown")
def shutdown():
    print("Server arrestato.")
    return "Server arrestato."

if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.125")
