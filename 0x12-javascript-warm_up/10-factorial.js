#!/usr/bin/node
function factorial (x) {
  if (x === 0 || isNaN(x) === true) {
    return 1;
  }
  return x * factorial(x - 1);
}
console.log(factorial(process.argv[2]));
