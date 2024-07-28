#!/usr/bin/python3
"""A script that starts a Flask web application
The web application is listening on 0.0.0.0 port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Return the string 'Hello HBNB!' when queried"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Return the string 'HBNB' when queried"""
    return "HBNB"


@app.route("/c/<text>")
def c_with_Text(text):
    """Return the formatted text as required when queried"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route("/python/<text>")
def python_with_Text(text="is cool"):
    """Return the 'Python' + formatted text variable when queried"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def n_is_number(n):
    """Return 'n is a number' on if variable n is a valid integer"""
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=None)
