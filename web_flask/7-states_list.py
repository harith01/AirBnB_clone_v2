#!/usr/bin/python3
"""Starts a Flask web app"""

from models import *
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def display_states():
    """Display HTML page containing list of State objects"""
    states = sorted(list(storage.all('States').values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
