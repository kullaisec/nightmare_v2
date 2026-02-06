from flask import Flask
from routes.profile import profile
from routes.admin import admin_panel
from routes.payments import transfer
from oauth.oauth_routes import oauth_start
from oauth.oauth_client import oauth_callback

app = Flask(__name__)

@app.route("/profile")
def profile_route():
    return profile()

@app.route("/admin")
def admin_route():
    return admin_panel()

@app.route("/transfer", methods=["POST"])
def transfer_route():
    return transfer()

@app.route("/oauth/start")
def oauth_start_route():
    return oauth_start()

@app.route("/callback")
def oauth_callback_route():
    return oauth_callback()

if __name__ == "__main__":
    app.run(debug=True)