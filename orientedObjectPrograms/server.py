from flask import Flask
import sys, os
from sys import exit
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

if (__name__ == "__main__"):
    app.run()