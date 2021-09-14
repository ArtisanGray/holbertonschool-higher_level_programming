#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = -1;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const item in data.results) {
    for (const car in data.results[item].characters) {
      if (car === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
