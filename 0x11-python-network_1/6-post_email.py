#!/usr/bin/python3
"""
script that:
- takes in a URL and email address as args
- sends a POST request and pass URL with the email as a parameter
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
