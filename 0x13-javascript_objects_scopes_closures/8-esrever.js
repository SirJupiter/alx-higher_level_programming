#!/usr/bin/node

exports.esrever = function (list) {
  if (Array.isArray(list)) {
    const arrayCopy = [...list];

    return arrayCopy.reverse();
  }
};
