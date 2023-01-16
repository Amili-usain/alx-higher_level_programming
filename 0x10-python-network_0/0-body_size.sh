#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
