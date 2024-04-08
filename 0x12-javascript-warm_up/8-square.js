#!/usr/bin/node

if (!process.argv[2] || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
  return;
}

const size = parseInt(process.argv[2]);

if (size < 1) {
  return;
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
