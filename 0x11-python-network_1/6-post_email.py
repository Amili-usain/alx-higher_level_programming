#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email, and finally displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {'email': argv[2]}
    req = requests.post(argv[1], data)

    print(req.text)
