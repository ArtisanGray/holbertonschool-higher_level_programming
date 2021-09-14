#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const tasksCompleted = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const item in data) {
    if (data[item].completed === true) {
      if (tasksCompleted[data[item].userId]) {
        tasksCompleted[data[item].userId] += 1;
      } else {
        tasksCompleted[data[item].userId] = 1;
      }
    }
  }
  console.log(tasksCompleted);
});
