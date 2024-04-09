#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  if (Array.isArray(list)) {
    for (const element of list) {
      if (element === searchElement) {
        count++;
      }
    }
  }

  return count;
};
