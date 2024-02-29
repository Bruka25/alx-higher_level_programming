#!/bin/bash
# Bash script that uses curl to send a POST request to the specified URL ($1)
curl -s -H "Content-Type: bruka/json" -d "$(cat "$2")" "$1"
