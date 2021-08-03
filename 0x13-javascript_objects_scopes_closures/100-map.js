#!/usr/bin/node

const data = require('./100-data');
const flip = data.list.map(x => multi(data.list, x));

function multi (list, item) {
  return item * list.indexOf(item);
}
console.log(data.list);
console.log(flip);
