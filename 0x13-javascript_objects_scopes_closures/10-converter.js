#!/usr/bin/node
// Converts a number from base 10 to another base passed as arg with Closure

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
