#!/usr/bin/python3
"""
script that:
- takes in a URL arg
- sends a POST request to the passed URL
- takes email as a second arg
- displays body of response  in utf-8 response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
