#!/usr/bin/node
exports.esrever = function (list) {
  const templ = [];
  for (let i = list.length - 1; i >= 0; i--) {
    templ.push(list[i]);
  }
  return templ;
};
