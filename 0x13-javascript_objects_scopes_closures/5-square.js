#!/usr/bin/node
// Creates a Square class that extends Rectangle class

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
