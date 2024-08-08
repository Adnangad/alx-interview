#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const filmId = process.argv[2].toString();
const url = 'https://swapi-api.alx-tools.com/api/films/';
const compUrl = url.concat(filmId);

function getNames (elem, callback) {
  // retreives the characters names
  let rem = elem.length;
  const names = [];
  elem.forEach((charUrl, index) => {
    request(charUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        rem -= 1;
      } else {
        const charName = JSON.parse(body);
        names[index] = charName.name;
      }
      rem -= 1;
      if (rem === 0) {
        callback(names);
      }
    });
  });
}
request(compUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    getNames(data.characters, (names) => {
      names.forEach((name) => console.log(name));
    });
  }
});
