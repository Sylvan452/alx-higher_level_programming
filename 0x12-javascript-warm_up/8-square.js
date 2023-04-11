#!/usr/bin/node
const process = require('process');
const args = process.argv;

let arr = [];
const size = parseInt(args[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      arr.push('X');
    }
    console.log(arr.join(''));
    arr = [];
  }
}

