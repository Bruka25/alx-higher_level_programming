#!/usr/bin/python3
"""Python script that sends POST request to the passed parameter with
   email as its parameter
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
