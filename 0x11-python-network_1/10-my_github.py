#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses the Github API
to display your id
"""
import requests
from pprint import pprint

# github username
username = "mcsepro"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)
