#!/usr/bin/node

// Script that prints the rectangle with 'X'
// This script takes width and height as parameters

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let j = 0;
      for (; j < this.width; j++) {
        process.stdout.write('X');
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }
};
