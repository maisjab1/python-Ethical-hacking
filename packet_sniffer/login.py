# test_server.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    '''

@app.route("/login", methods=["POST"])
def login():
    return "Login received"

app.run(host="0.0.0.0", port=8080)

