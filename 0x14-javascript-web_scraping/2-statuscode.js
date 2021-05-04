#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err !== null) {
    console.error('error:', err);
  }
  console.log('code:', response.statusCode);
});
