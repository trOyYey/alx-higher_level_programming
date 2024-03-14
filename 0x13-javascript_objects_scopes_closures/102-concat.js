#!/usr/bin/node

const fs = require('fs');
const Files = process.argv;

if (Files.length === 5) {
  let text = fs.readFileSync(Files[2], 'utf8');
  text += fs.readFileSync(Files[3], 'utf8');
  fs.writeFileSync(Files[4], text);
} else {
  console.log('Usage: fileName firstfile secondFile destFile');
}
