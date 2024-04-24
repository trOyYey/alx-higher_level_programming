#!/usr/bin/node

const arg = process.argv;
const RQ = require('request');

RQ.get(arg[2]).on('response', (res) => {
  console.log('code: ' + res.statusCode);
});
