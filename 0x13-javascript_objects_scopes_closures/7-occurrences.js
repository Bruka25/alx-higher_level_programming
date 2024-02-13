#!/usr/bin/node
// Returns the number of occurrences of an element in a list

exports.nbOccurences = function (list, searchElement) {
  return list.filter(o => o === searchElement).length;
};
