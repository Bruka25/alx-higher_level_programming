#!/bin/bash
# Bash script use curl to send a DELETE request (-X DELETE) to the URL provided as the first argument ($1)
curl -s "$1" -X DELETE
