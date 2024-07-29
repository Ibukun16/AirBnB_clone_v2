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
    sort_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('states_list.html', sort_states=sort_states)


@app.teardown_appcontext
def close(self):
    """Closing and cleaning up session current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
