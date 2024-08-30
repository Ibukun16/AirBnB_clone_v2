#!/usr/bin/python3
"""A script that starts a Flask web application
The web application is listening on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return an html page with states and cities"""
    states = storage.all(State)
    # sort State object by name in alphabetical order
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Closing and cleaning up current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
