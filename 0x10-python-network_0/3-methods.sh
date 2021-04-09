#!/bin/bash
# gets all http methods that the server will accept
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
