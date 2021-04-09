#!/bin/bash
# sends a POST request
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
