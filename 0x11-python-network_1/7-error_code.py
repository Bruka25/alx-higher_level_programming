#!/usr/bin/python3
"""Python scirpt that sends a request and displays the
   body of the response using requests module
   prints the error status codes if they are greater than
   or equal to 400
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
