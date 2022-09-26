#!/usr/bin/python3
"""Use requests package to make a get request to given URL
"""
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
