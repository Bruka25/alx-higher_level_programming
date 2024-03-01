#!/usr/bin/python3
"""python script that takes persons github username and
   password and displays it's id using GitHub API
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    try:
        print(req['id'])
    except:
        print("None")        
