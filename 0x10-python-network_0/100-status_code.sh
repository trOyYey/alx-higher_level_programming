#!/bin/bash
#Bash script that sends a request to a URL and displays status code
curl -so /dev/null -w "%{http_code}" "$1"
