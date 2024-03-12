#!/usr/bin/node

const args = process.argv.slice(2, 4);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(args[0], args[1]);
