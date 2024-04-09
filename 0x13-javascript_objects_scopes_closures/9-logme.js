#!/usr/bin/node

exports.logMe = function (item) {
  let count = 0;

  return function (item) {
    console.log(count++ + ': ' + item);
  };
}();
