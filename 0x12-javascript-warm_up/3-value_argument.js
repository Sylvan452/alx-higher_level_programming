#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args[2] !== undefined) {
  console.log(args[2]);
}else if (args[2] === undefined) {
  console.log('No argument');
}
