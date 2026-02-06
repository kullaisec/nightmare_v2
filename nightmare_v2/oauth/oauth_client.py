from flask import request
from oauth.state_store import valid

def oauth_callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if not valid(state):
        return "Invalid state", 400

    return "Logged in"