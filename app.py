from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hw():
    return dict(message="Hello world")

app.run()