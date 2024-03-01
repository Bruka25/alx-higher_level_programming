#!/usr/bin/python3

"""Python script that takes in url, sends the
   request to the url and displays the body
   of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
