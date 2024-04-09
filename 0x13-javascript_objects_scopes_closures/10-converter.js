#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    const digits = '0123456789ABCDEF';

    if (number === 0) {
      return '0';
    }

    let result = '';
    while (number > 0) {
      const remainder = number % base;
      result = digits[remainder] + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
