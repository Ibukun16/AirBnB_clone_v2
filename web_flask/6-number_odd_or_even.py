#!/usr/bin/python3
"""A script that starts a Flask web application
The web application is listening on 0.0.0.0 port 5000
"""

from flask import Flask, render_template
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
def c_with_Text(text):
    """Return the formatted text as required when queried"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_Text(text="is cool"):
    """Return the 'Python' + formatted text variable when queried"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """Return 'n is a number' on if variable n is a valid integer"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """Return an HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """Return the HTML page with info below only if n is an integer:
    H1 tag: "Number: n is even|odd" inside the tag BODY
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
