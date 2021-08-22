#!/bin/bash
# this script returns the allowed HTTP methods on the specified URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
