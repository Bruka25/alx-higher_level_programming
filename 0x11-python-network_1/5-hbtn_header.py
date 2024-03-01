#!/usr/bin/python3
"""Python script that displays the value of the variable in the header
   using the package requests
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
