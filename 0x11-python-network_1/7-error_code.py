#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays:
- the body of the response if there are no errors and
- prints Error code: If the HTTP status code is >= to 400
followed by the value of the HTTP status code.
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
