#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
var tasks_Completed = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const item in data) {
    if (data[item].completed === true) {
      if (tasks_Completed[data[item].userId]) {
        tasks_Completed[data[item].userId] += 1;
      } else {
        tasks_Completed[data[item].userId] = 1;
      }
    }
  }
  console.log(tasks_Completed);
});
