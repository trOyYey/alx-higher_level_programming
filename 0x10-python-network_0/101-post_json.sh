#!/bin/bash
# Bash script that sends JSON POST to URL and displays body of respo
curl -sH "Content-Type: application/json" -d "@$2" "$1"
