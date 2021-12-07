from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hw():
    return dict(message="Hello world")

if __name__ == "__main__":
    app.run(port=int(os.getenv('PORT')))