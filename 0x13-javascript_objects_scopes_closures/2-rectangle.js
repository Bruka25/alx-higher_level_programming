#!/usr/bin/node
// Javascript that checks if the arguments of
// of the rectangle are positive integers

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
