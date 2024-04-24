#!/usr/bin/node

const arg = process.argv;
const RQ = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[2];
RQ(url, (err, res, body) => {
  if (err) return console.log(err);
  JSON.parse(body).characters.forEach(charact => {
    RQ(charact, (error, resp, bd) => {
      if (error) return console.log(error);
      console.log(JSON.parse(bd).name);
    });
  });
});
