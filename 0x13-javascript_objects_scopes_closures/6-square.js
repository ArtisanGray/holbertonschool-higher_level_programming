#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0, str = ''; i < this.height; i++, str = '') {
      for (let j = 0; j < this.width; j++) {
        str = str + c;
      }
      console.log(str);
    }
  }
};
