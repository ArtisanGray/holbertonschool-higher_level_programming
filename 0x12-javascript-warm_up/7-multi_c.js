#!/usr/bin/node
if (process.argv[2] != null || !isNaN(process.argv[2])) {
  const occ = parseInt(process.argv[2]);
  for (let i = 0; i < occ; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
