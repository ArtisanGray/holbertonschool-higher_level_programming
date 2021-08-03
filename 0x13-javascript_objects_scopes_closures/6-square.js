#!/usr/bin/node

const oldSqr = require('./5-square');
module.exports = class Square extends oldSqr {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
