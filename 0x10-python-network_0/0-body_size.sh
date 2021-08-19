#!/bin/bash
#requests a url and displays the size of the body of the response.
if [ "$#" -ne 2 ]; then
  curl -sI "$1" | grep -i Content-Length
fi
