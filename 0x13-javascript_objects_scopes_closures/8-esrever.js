#!/usr/bin/node

exports.esrever = function (list) {
  if (Array.isArray(list)) {
    const arrayCopy = [];

    for (let i = list.length - 1; i >= 0; i--) {
      arrayCopy.push(list[i]);
    }

    return arrayCopy;
  }
};
