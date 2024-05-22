#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    let count = 0;
    let result = {};

    for (let i = 1; i <= 10; i++) {
      for (const item of data) {
        if (item.userId == i && item.completed == true) count++;
      }

      result[`${i}`] = count;
      count = 0;
    }

    console.log(result);
  }
});
