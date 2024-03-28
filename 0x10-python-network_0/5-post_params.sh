#!/bin/bash
# script that will send post request and displays the body of a response
curl -Ls -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
