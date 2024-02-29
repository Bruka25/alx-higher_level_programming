#!/bin/bash
# Bash scrript to take URL, sends GET request and displays the body of the response
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
