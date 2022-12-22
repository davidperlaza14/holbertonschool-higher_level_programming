#!/usr/bin/node
const myVar = process.argv[2];
if (isNaN(myVar) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < myVar; x++) {
    console.log('C is fun');
  }
}