#!/usr/bin/node
const fs = require('fs');
const rq = require('request');
rq(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
