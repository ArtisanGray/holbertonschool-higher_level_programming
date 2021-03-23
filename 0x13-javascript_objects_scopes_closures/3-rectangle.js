#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0, str = ''; i < this.height; i++, str = '') {
      for (let j = 0; j < this.width; j++) {
        str = str + 'X';
      }
      console.log(str);
    }
  }
};
