#!/bin/bash
# write a Bash script that sends a DELETE request to the URL passed as the first argument
curl -Ls -X DELETE "$1"
