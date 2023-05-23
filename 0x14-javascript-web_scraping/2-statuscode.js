#!/usr/bin/node
const rq = require('request');
rq.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
