#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Not a number');
  return;
}

const num = Math.floor(parseFloat(process.argv[2], 10));
// Check if the input is a valid number
if (isNaN(num)) {
  console.log('Not a number');
  return;
}

console.log('My number: ' + num);
