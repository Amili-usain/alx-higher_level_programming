#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status and displays
The body of the response with tabulation before -.
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
