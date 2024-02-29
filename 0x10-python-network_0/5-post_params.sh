#!/bin/bash
# Bash script that uses curl to send a POST request (-X POST) to the specified URL ($1)
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
