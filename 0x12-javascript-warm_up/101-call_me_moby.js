#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
      func();
    }
  }
};
