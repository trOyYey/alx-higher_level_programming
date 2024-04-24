#!/usr/bin/node

const arg = process.argv;
const RQ = require('request');

RQ(arg[2], (err, res, body) => {
  if (err) return console.log(err);
  const result = {};
  JSON.parse(body).forEach(task => {
    const index = task.userId;
    if (task.completed) {
      result[index] = result[index] ? result[index] + 1 : 1;
    }
  });
  console.log(result);
});
