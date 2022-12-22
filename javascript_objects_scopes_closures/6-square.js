#!/usr/bin/node
const BSquare = require('./5-square');
module.exports = class Square extends BSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
