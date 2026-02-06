from utils.request import parse_body
from middleware.proxy_headers import get_real_content_length

def handle_request(raw_body):
    length = get_real_content_length()
    body = parse_body(raw_body, length)
    return body