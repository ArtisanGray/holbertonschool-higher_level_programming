#!/usr/bin/node

const data = require('./100-data');
const flip = data.list.map(x => multi(data.list, x));

function multi (list, item) {
  const temp = list.indexOf(item);
  return item * temp;
}
console.log(data.list);
console.log(flip);
