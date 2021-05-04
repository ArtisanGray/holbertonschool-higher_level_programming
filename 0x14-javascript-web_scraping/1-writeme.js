#!/usr/bin/node

const fs = require('fs');

fs.appendFile(process.argv[2], process.argv[3], 'utf-8', function (err, data) {
  if (err !== null) {
    console.log(err);
    return;
  }
  console.log(data);
});
