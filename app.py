import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """ Store messages in the main list """
    messages.append(f"{username}: {message}")


def get_all_messages():
    """ Gets all of the messages and displays it in a new line"""
    return "<br>".join(messages)

@app.route("/")
def index():
    """Main page with instrictions"""
    return "<h1>To send a message use /USER/MESSAGE/</h1>"


@app.route("/<username>")
def user(username):
    """ Display chat messages """
    return f"<h1>Welcome {username}</h1> {get_all_messages()}"


@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect back to the chat page """
    add_messages(username, message)
    return redirect(f"/{username}")


if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)