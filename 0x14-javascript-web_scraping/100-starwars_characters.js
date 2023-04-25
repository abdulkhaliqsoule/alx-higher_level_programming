#!/usr/bin/node
const request = require('request');
const address = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).characters;
    for (const i of results) {
      request(i, (e, r, b) => console.log(JSON.parse(b).name));
    }
  }
});
