#!/usr/bin/node

const fs = require('fs');
const content = process.argv[3];
const filename = process.argv[2];

fs.writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
});
