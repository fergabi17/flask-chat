import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    # Main page with instrictions
    return "<h1>To send a message use /USER/MESSAGE/</h1>"


@app.route("/<username>")
def user(username):
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return f"{username}: {message}"


if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)