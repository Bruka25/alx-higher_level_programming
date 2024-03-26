#!/usr/bin/node
const req = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
