#!/usr/bin/node

const string = process.argv;
let len = 0;
while (string[len] !== undefined) {
  len++;
}
if (len < 3) {
  console.log('No argument');
} else {
  console.log(string[2]);
}
