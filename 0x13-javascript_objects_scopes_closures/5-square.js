#!/usr/bin/node

// Javascript square class that inherits from rectangle

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
