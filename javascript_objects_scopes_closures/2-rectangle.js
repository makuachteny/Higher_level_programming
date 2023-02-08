#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (
      w <= 0 ||
      h <= 0 ||
      typeof w !== 'number' ||
      typeof h !== 'number' ||
      !Number.isInteger(w) ||
      !Number.isInteger(h)
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
