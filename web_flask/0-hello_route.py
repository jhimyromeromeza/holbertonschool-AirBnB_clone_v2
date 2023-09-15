#!/usr/bin/python3
"""
this is a simple flask module
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    This function handles the root path of the application and returns the message 'Hello HBNB!'. 
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
