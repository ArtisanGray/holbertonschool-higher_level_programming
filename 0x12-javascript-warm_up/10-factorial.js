#!/usr/bin/node

function factorial (n) {
  if (n > 0) {
    return (n * factorial(n - 1));
  } else if (n === 0 || isNaN(n) === true) {
    return (1);
  }
  return (-1);
}
console.log(factorial(parseInt(process.argv[2])));
