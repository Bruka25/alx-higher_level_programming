#!/usr/bin/node
// Function that returns a number from
// base 10 to other base specified as
// an argument

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
