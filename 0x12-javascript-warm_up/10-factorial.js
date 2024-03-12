#!/usr/bin/node

const num = process.argv[2];

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(myFactorial(num));
}
function myFactorial (num) {
  if (num === 1) {
    return (1);
  }
  return (num * myFactorial(num - 1));
}
