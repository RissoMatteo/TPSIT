from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Percorso al database SQLite
DATABASE = 'login_db.db'


@app.route('/')
def home():
    return render_template('login.html')

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
        return redirect(url_for('home'))
    else:
        print("Login failed!")
        flash('Invalid username or password!', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
