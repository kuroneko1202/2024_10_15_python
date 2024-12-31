from flask import Flask

app = Flask(__name__)

@app.route("/")
def Index():
    return "<h1>Hello, 你好!</h1>" 

@app.route("/hello")
def hello():
    return "Hello, World!!!!" 