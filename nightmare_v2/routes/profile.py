from flask import request
from middleware.cache_middleware import cache_response

@cache_response
def profile():
    user = request.headers.get("X-User", "guest")
    return f"Hello {user}"