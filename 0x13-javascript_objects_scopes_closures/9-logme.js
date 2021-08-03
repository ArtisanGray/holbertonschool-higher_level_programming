#!/usr/bin/node
let temp = 0;
exports.logMe = function (item) {
  temp++;
  console.log(temp + ': ' + item);
};
