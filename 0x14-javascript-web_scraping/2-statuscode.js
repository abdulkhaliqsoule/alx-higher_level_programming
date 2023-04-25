#!/usr/bin/node
const request = require('request');
const address = process.argv[2];
request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
