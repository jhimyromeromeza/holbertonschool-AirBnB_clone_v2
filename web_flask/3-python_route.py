#!/usr/bin/python3}
""" 
this is a simple module with route
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    This function handles the root path of the application and returns the message 'Hello HBNB!'.
    """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashe=False)
def hbnb():
    """
    This function manage a route hbnb and returns the message 'HBNB'.
    """
    return "HBNB"
@app.route('/c/<text>')
def c_text(text):
    """
    This is a function that returns a text according to parameter. 
    """
    return "C {}".format(text.replace('_', ' '))
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    This is a function that returns a text according to parameter. 
    """
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)