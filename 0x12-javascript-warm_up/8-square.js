#!/usr/bin/node

if (!process.argv[2] || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
}

const size = parseInt(process.argv[2]);

if (size > 0) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
