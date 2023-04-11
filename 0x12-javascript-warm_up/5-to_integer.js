#!/usr/bin/node
cost process = require('process');
const args = process.argv;

if (isNAN(args[2])){
	console.log('Not a number');
}else {
	console.log('My number',args[2]);
}
