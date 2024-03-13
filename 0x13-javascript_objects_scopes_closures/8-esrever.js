#!/usr/bin/node

exports.esrever = function (list) {
  const revs = [];
  let i = list.length - 1;
  while (i > -1) {
    revs.push(list[i]);
    i--;
  }
  return (revs);
};
