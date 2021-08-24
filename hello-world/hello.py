from flask import Flask

"""
https://flask.palletsprojects.com/en/2.0.x/quickstart/
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"