from flask import request
from middleware.cache_middleware import cache_response

@cache_response
def admin_panel():
    role = request.headers.get("X-Role", "user")

    if role != "admin":
        return "Forbidden", 403

    return "Welcome to admin panel"