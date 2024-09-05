from datetime import datetime, timedelta
import random
import re
from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
from pymongo import MongoClient
import bcrypt
import os
from config import getProducts

app = Flask(__name__)
app.secret_key = os.urandom(24)

MONGO_DB_URI = '' # your mongo db URI 

client = MongoClient(MONGO_DB_URI)
db = client['data']
users = db['users']

signup_blueprint = Blueprint('signup', __name__)
login_blueprint = Blueprint('login', __name__)

@app.route('/')
def home():
    return render_template('index.html')

attempts = {}
delay = random.randint(5, 10)
COOLDOWN_PERIOD = timedelta(minutes=delay)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        now = datetime.now()

        if username in attempts:
            current_attempts, last_attempt_time = attempts[username]
            if current_attempts >= 5:
                if now - last_attempt_time < COOLDOWN_PERIOD:
                    flash("Too many failed login attempts. Please try again later.", "danger")
                    return redirect(url_for('login'))
                else:
                    attempts[username] = [0, now]

        user = users.find_one({'username': username})

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            if username in attempts:
                del attempts[username]
            flash("Login successful! Redirecting...", "success")
            return redirect(url_for('home'))
        else:
            if username in attempts:
                current_attempts, last_attempt_time = attempts[username]
                attempts[username] = [current_attempts + 1, last_attempt_time]
            else:
                attempts[username] = [1, now]
            flash("Invalid username or password.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9.]{3,12}$', username) is not None

def is_valid_password(password):
    return 8 <= len(password) <= 12

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if not is_valid_email(email):
            flash("Invalid email format.", "danger")
            return redirect(url_for('signup'))

        if not is_valid_username(username):
            flash("Username must be 3-12 characters long and can only contain letters, numbers, and periods ('.').", "danger")
            return redirect(url_for('signup'))

        if not is_valid_password(password):
            flash("Password must be 8-12 characters long.", "danger")
            return redirect(url_for('signup'))

        existing_user = users.find_one({'email': email})
        if existing_user:
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for('signup'))

        if users.find_one({'username': username}):
            flash("Username already reserved. Please choose a different username.", "danger")
            return redirect(url_for('signup'))

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        users.insert_one({
            'email': email,
            'username': username,
            'password': hashed_password
        })

        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for('signup'))

    return render_template('signup.html')

app.register_blueprint(signup_blueprint)
app.register_blueprint(login_blueprint)



if __name__ == '__main__':
    app.run(debug=True, port=5089)
