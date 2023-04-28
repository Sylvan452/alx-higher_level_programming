#!/usr/bin/python3
"""
script that:
- takes in a URL arg
- sends a POST request to the passed URL
- manages HTTPError exceptions and print: Error code
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
