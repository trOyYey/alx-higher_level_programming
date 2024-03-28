#!/bin/bash
# cURLing a JSON file
curl -sH "Content-Type: application/json" -d "@$2" "$1"
