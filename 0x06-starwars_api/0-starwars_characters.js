#!/usr/bin/node
const httpRequest = require('request');
const BASE_API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  httpRequest(`${BASE_API_URL}/films/${process.argv[2]}/`, (error, _, responseBody) => {
    if (error) {
      console.log(error);
    }
    const characterUrls = JSON.parse(responseBody).characters;
    const characterPromises = characterUrls.map(
      characterUrl => new Promise((resolve, reject) => {
        httpRequest(characterUrl, (promiseError, __, characterData) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(characterData).name);
        });
      }));

    Promise.all(characterPromises)
      .then(characterNames => console.log(characterNames.join('\n')))
      .catch(promiseAllError => console.log(promiseAllError));
  });
}
