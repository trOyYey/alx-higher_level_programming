#!/usr/bin/node

const RQ = require('request');

let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
main();

function getbd (value) {
  return new Promise((resolve, reject) => {
    RQ(value, (err, resp, body) => {
      if (err) reject(err);
      resolve(JSON.parse(body));
    });
  });
}

async function main () {
  let movie = await getbd(url);
  movie = movie.characters;
  for (let i = 0; i < movie.length; i++) {
    const name = await getbd(movie[i]);
    console.log(name.name);
  }
}
