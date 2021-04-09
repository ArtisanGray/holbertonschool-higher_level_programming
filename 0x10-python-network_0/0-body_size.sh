#!/bin/bash
# displays the size of body in http response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
