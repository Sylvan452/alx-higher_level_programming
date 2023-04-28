#!/usr/bin/python3
"""
 Script that:
- gets URL from command line,
- sends a request to the URL and displays respons
- display  X-Request-Id variable found in the header
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
