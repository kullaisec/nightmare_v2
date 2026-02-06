from flask import request, redirect
from oauth.state_store import save

def oauth_start():
    state = request.args.get("state") 
    save(state)

    return redirect(
        "https://oauth.example.com/auth"
        f"?client_id=abc"
        f"&redirect_uri=http://localhost/callback"
        f"&state={state}"
    )