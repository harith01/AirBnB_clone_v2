#!/usr/bin/python3
"""This script starts a Flask web application
Listening on 0.0.0.0, port 5000

Routes:
  /: display "Hello HBNB!"
  /hbnb: display "HBNB"
  /c/<text>: display "C" followed by the value of <text>
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays 'C' follwed by the value of variable text"""
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
