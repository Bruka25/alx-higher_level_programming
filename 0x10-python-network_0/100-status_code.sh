#!/bin/bash
# Bash request that sends GET request to a given URL and display only the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
