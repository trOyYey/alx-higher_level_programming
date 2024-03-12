#!/usr/bin/node

const args = process.argv.slice(2);
const storage = [0, 0];
let i = 0;

while (args[i] !== undefined) {
  const n = parseInt(args[i]);
  let j = 0;
  while (storage[j] !== undefined) {
    if (n >= storage[j]) {
      if (j === 0) {
        storage[1] = storage[0];
        storage[0] = n;
      } else {
        storage[j] = n;
      }
      break;
    }
    j++;
  }
  i++;
}
console.log(storage[1]);
