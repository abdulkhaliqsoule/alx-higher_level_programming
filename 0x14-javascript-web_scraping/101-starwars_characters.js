#!/usr/bin/node
const request = require('request');
const address = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).characters;
    const promises = [];
    for (const i of results) {
      promises.push(new Promise(function (resolve, reject) {
        request(i, (e, r, b) => resolve(JSON.parse(b).name));
      }));
    }
    Promise.all(promises).then((a) => {
      for (const i of a) { console.log(i); }
    });
  }
});
