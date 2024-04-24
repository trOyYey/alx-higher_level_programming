#!/usr/bin/node

const fs = require('fs');
const arg = process.argv;

try {
  fs.writeFileSync(arg[2], arg[3], 'utf8');
} catch (err) {
  console.log(err);
}
