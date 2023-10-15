from crypt import methods
from distutils.log import debug
import email
from email import message
from tkinter import INSERT
from flask import Flask, flask , render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/', methods=['post'])
def index():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    # return render_template('index.html')
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?,?)" , (name,email,subject,message) )
    c.close()
    return render_template("index.html" , msg = "Your message have been succesfully delivered !")
 
if __name__ == '__main__':
    app.run(debug-True)