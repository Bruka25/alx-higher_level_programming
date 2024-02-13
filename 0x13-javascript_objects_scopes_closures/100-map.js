#!/usr/bin/node
// Javascript for mapping data
// It returns the the item multiplied by index

const listMap = require('./100-data.js').list;
console.log(listMap);
console.log(listMap.map((item, index) => item * index));
