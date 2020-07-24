# !/usr/bin/env python
import requests


def make_request(url):
    try:
        return response.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
