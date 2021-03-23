#!/usr/bin/node

if (isNaN(parseInt(process.argv[2])) === true || !process.argv[2]) {
  console.log('Missing size');
} else {
  for (let x = 0, str = ''; x < parseInt(process.argv[2]); x++, str = '') {
    for (let y = 0; y < parseInt(process.argv[2]); y++) {
      str = str + 'X';
    }
    console.log(str);
  }
}
