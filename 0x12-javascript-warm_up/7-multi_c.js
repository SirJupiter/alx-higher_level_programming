#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}

const count = parseInt(process.argv[2]);

if (count > 0) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
