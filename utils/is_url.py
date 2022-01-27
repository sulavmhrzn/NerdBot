from urllib.parse import urlparse


def is_url(url):
    """Given an URL return True if it is a valid url else False"""
    result = urlparse(url)
    if not all([result.scheme, result.netloc]):
        return False
    return True
