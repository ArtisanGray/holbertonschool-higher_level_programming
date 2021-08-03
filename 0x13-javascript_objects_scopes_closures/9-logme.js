#!/usr/bin/node
let temp = -1;
exports.logMe = function (item) {
  temp++;
  console.log(temp + ': ' + item);
};
