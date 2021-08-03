#!/usr/bin/node
let length = -1;
const data = require('./100-data');
const flip = data.list.map(x => multi(data.list, x));

function multi (list, item) {
  length++;
  return item * length;
}
console.log(data.list);
console.log(flip);
