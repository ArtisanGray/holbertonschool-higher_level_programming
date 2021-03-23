#!/usr/bin/node

const arr = [];
if (process.argv.length <= 3) {
  console.log('0');
} else {
  for (const item in process.argv) {
    arr.push(isNaN(parseInt(process.argv[item])) ? 0 : parseInt(process.argv[item]));
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
