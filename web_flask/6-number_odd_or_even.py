#!/usr/bin/python3
""" 
this is a simple module with route
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello ():
    """
    This function handles the root path of the application and returns the message 'Hello HBNB!'.
    """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb ():
    """
    This function manage a route hbnb and returns the message 'HBNB'.
    """
    return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def c_text (text):
    """
    This is a function that returns a text according to parameter. 
    """
    return "C {}".format(text.replace('_', ' '))
@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/pyhon/<text>', strict_slashes=False)
def python_text (text):
    """
    This is a function that returns a text according to parameter. 
    """
    return "Python {}".format(text.replace('_', ' '))
@app.route('/number/<int:n>', strict_slashes=False)
def number_n (n):
    """
    This is a function that returns a text according to parameter integer. 
    """
    return "{} is a number".format(n)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template (n):
    """
    function that outputs an html template passing the variable n as a parameter.a 
    """
    return render_template('5-number.html', n=n)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even (n):
    """
    function that outputs an html template passing the variable n as a parameter conditional. 
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)