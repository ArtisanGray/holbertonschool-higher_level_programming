#!/usr/bin/node
if (process.argv.length > 3) {
  let newarg = process.argv.slice(2);
  newarg.sort(function (a, b) { return b - a; });
  console.log(newarg[1]);
} else {
  console.log(0);
}
