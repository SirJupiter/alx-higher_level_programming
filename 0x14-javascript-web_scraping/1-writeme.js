#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const theString = process.argv[3];

if (filePath && theString) {
  fs.writeFile(filePath, theString, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
}
