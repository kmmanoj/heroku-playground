from flask import Flask

app = Flask(__name__)

@app.route("/")
def hw():
    return dict(message="Hello world")

app.run(port=5000)