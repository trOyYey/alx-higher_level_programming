#!/usr/bin/node

const arg = process.argv;
const RQ = require('request');

RQ('https://swapi-api.alx-tools.com/api/films/' + arg[2], (err, res, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
