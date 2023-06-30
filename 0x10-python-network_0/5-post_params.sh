#!/bin/bash
# script that takes isn a URL, sends a Post request to the passed URL, and displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
