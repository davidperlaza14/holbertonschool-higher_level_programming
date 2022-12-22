#!/usr/bin/node
function nextBiggest (arr) {
  let max = 0; let result = 0;

  for (const value of arr) {
    const i = Number(value);

    if (i > max) {
      [result, max] = [max, i];
    } else if (i < max && i > result) {
      result = i;
    }
  }

  return result;
}

console.log(nextBiggest(process.argv));
