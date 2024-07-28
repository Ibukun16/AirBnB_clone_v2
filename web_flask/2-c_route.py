#!/usr/bin/python3
"""A script that starts a Flask web application
The web application is listening on 0.0.0.0 port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return the string 'Hello HBNB!' when queried"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return the string 'HBNB' when queried"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Return the formatted text as required when queried"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
