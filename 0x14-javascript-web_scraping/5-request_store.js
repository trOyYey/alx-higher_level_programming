#!/usr/bin/node

const arg = process.argv;
const RQ = require('request');
const fs = require('fs');

RQ(arg[2], (err, res, body) => {
  if (err) console.log(err);
  fs.writeFile(arg[3], body, { flag: 'w+', encoding: 'utf-8' }, (err) => {
    if (err) console.log(err);
  });
});
