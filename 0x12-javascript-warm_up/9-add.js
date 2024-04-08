#!/usr/bin/node

function add(a, b) {
  if (!isNaN(a) && !isNaN(b)) return a + b;
}

if (!process.argv[2] || !process.argv[3]) {
  console.log('NaN');
  return;
}

const numOne = parseInt(process.argv[2], 10);
const numTwo = parseInt(process.argv[3], 10);

console.log(add(numOne, numTwo));
