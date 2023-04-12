#!/usr/bin/node
exports.esrever = function(list) {
  const alteredList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    alteredList.push(list[i]);
  }

  return alteredList;
};

