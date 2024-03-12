#!/usr/bin/node

const itr = process.argv[2];

if (isNaN(itr)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < itr) {
    console.log('X'.repeat(itr));
    i++;
  }
}
