#!/bin/bash
# bash script hat takes in a URL, sends a request to that URL,
#+ and sends the size of the body response
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
