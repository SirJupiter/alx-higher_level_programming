#!/usr/bin/node

let result;

if (!process.argv[2]) {
  result = 1;
}

function fact (num) {
  if (num === 1) {
    return 1;
  }

  return num * fact(num - 1);
}

const compute = parseInt(process.argv[2]);

if (!isNaN(compute)) {
  result = fact(compute);
}

console.log(result);
