#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    for (const movie of data.results) {
      for (const char of movie.characters) {
        if (char.includes(18)) count++;
      }
    }

    console.log(count);
  }
});
