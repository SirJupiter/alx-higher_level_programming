#!/usr/bin/node
//  script computes the number of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // console.log(body);
    const data = JSON.parse(body);

    let result = {};

    for (const item of data) {
      if (item.completed) {
        if (!result[item.userId]) {
          result[item.userId] = 1;
        } else {
          result[item.userId] += 1;
        }
      }
    }

    console.log(result);
  }
});
