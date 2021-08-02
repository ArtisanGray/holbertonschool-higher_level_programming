#!/usr/bin/node
if (process.argv[2] != null && !isNaN(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  let str = '';
  for (let i = 0; i <= size; i++) {
    if (str.length > 0) {
      console.log(str);
    }
    str = '';
    for (let j = 0; j < size; j++) {
      str = str + 'X';
    }
  }
} else {
  console.log('Missing size');
}
