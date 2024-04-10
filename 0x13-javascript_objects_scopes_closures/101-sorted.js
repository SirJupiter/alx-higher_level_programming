#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = [];

for (const key of Object.keys(dict)) {
  if (!newDict.length) {
    newDict.push(dict[key]);
  } else {
    for (const element of newDict) {
      if (element !== dict[key]) {
        newDict.push(dict[key]);
      }
    }
  }
}

const obj = {};

for (const item of newDict) {
  obj[item] = [];

  for (const key of Object.keys(dict)) {
    if (dict[key] === item) {
      obj[item].push(key);
    }
  }
}

console.log(obj);
