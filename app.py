from flask import Flask, render_template, request
from functions import add_email

import random

app = Flask(__name__)
app.secret_key = str(random.randint(1, 20))


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        email = request.form['email']
        add_email(email)

    return render_template('index.html')
