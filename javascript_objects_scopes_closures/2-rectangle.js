#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (
      width === 0 ||
      height === 0 ||
      typeof width !== 'number' ||
      typeof height !== 'number'
    ) {
      this.width = 0;
      this.height = 0;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
