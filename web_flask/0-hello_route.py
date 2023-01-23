#!/usr/bin/python3
"""Starts a flask web app
The app is  listening on 0.0.0.0, port 5000
Has a home route displaying “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greetings():
    """ Greets Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
