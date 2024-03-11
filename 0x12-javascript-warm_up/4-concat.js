#!/usr/bin/node

const args = process.argv;
if (args[2] === undefined) { args[2] = 'undefined'; }
if (args[3] === undefined) { args[3] = 'undefined'; }
const string = args[2] + ' ' + 'is' + ' ' + args[3];
console.log(string);
