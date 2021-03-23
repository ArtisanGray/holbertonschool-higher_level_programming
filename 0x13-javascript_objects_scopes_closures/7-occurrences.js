#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;

  for (const item in list) {
    if (searchElement === list[item]) {
      occ++;
    }
  }
  return (occ);
};
