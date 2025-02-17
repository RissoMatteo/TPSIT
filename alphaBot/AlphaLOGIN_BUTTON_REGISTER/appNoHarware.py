from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import sqlite3
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'login_db.db'

# Funzioni di movimento del bot (senza hardware per simulazione)
def move_forward():
    print("Muovendo avanti")
    time.sleep(0.5)

def move_backward():
    print("Muovendo indietro")
    time.sleep(0.5)

def move_left():
    print("Girando a sinistra")
    time.sleep(0.5)

def move_right():
    print("Girando a destra")
    time.sleep(0.5)

def stop():
    print("Stop")

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
        flash('Login successful!', 'success')
        response = make_response(redirect(url_for('control')))
        response.set_cookie('user', username)  # Salva l'utente nel cookie
        return response
    else:
        flash('Invalid username or password!', 'danger')
        return redirect(url_for('home'))

# Rotta per controllare il bot
@app.route('/control', methods=["GET", "POST"])
def control():
    user = request.cookies.get('user')  # Recupera l'utente dal cookie
    if not user:
        flash('You need to log in first!', 'warning')
        return redirect(url_for('home'))

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
    return render_template("index.html", user=user)  # Mostra il nome dell'utente nella pagina

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
    response.delete_cookie('user')  # Rimuove il cookie dell'utente
    flash('You have been logged out.', 'success')
    return response

# Rotta per spegnere il server (opzionale)
@app.route("/shutdown")
def shutdown():
    print("Server arrestato.")
    return "Server arrestato."


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
