#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const item in data.characters) {
    request(data.characters[item], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
