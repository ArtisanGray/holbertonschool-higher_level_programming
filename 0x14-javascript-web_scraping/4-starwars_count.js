#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
let tstr = '';
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const item in data.results) {
    for (const car in data.results[item].characters) {
      tstr = data.results[item].characters[car];
      if (tstr.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
