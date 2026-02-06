from flask import request
from middleware.csrf import csrf_protect

def transfer():
    if not csrf_protect():
        return "CSRF failed", 403

    amount = request.form["amount"]
    to = request.form["to"]
    return f"Transferred {amount} to {to}"