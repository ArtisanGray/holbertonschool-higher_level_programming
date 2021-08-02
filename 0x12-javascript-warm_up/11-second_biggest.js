#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log(0);
} else {
  const newarr = process.argv.sort(function (a, b) { return b - a; });
  console.log(newarr[3]);
}
