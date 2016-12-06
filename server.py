from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
app=Flask(__name__)
mysql=MySQLConnector(app, 'login_registration')
bcrypt=Bcrypt(app)
app.secret_key="MagicSecretKey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    return render_template('index.html')


app.run(debug=True)
