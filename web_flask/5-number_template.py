#!/usr/bin/python3
"""This script starts a Flask web application
Listening on 0.0.0.0, port 5000

Routes:
  /: display "Hello HBNB!"
  /hbnb: display "HBNB"
  /c/<text>: display "C" followed by the value of <text>
  /python/(<text>): display "Python" follwed by the varaibale <text>
  /number/n: display "n is a number" only if n is an int
  /number_template/n: display a HTML page only if n is an int
"""

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """Display "Python" followed by <text>"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """Display 'n is a number'"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_n_html(n):
    """Display a HTML page if n is an int"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
