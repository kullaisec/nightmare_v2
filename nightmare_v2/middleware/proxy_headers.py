from flask import request

def get_real_content_length():
    if "Content-Length" in request.headers:
        return int(request.headers["Content-Length"])
    return None