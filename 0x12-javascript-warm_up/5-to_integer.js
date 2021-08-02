#!/usr/bin/node
if (process.argv[2] != null) {
  console.log(!isNaN(process.argv[2]) ? ('My number: ' + parseInt(process.argv[2])) : 'Not a number');
} else {
  console.log('Not a number');
}
