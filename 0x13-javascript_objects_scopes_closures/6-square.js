#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    for (let i = 0, str = ''; i < this.height; i++, str = '') {
      for (let j = 0; j < this.width; j++) {
        str = str + c;
      }
      console.log(str);
    }
  }
};
