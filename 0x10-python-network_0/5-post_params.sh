#!/bin/bash
# this script sends data to the specified URL.
curl -sd "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
