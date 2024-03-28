#!/bin/bash
# script that takes in a URL and displays the size of the body of the response
curl -I "$1" -s | grep Content-Length | cut -d ' ' -f2
