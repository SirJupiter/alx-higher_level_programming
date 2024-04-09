#!/usr/bin/node

let bigNum;

if (process.argv.length <= 3) {
  bigNum = 0;
} else {
  const numArr = [];

  for (let i = 2; i < process.argv.length; i++) {
    numArr.push(parseInt(process.argv[i]));
  }

  numArr.sort((a, b) => a - b);

  bigNum = numArr[numArr.length - 2];
}

console.log(bigNum);
