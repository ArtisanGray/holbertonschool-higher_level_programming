#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let i = 0;
  for (; i < list.length; i++) {
    continue;
  }
  for (let j = i - 1; j >= 0; j--) {
    revList.push(list[j]);
  }
  return (revList);
};
