from database.conn import banco
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for, app,Flask
import os

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)




