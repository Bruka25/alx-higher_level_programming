#!/usr/bin/python3
"""python script that takes in a url, sends POST request
   and display the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post = {'email': email}
    res = requests.post(url, data=post)
    print(res.text)
