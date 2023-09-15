#!/usr/bin/python3
from flask import Flask
"""
this is a simple module with route
"""
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    This function handles the root path of the application and returns the message 'Hello HBNB!'.
    """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def display():
    """
    This function manahe a route hbnb and returns the message 'HBNB'.
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)