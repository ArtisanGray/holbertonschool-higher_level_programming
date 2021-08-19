#!/bin/bash
# this script grabs only the http response code of a request.
curl -s -o /dev/null -w "%{http_code}" $1
