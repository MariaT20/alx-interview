#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const movieEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieID;


request(movieEndPoint, (res, error, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrl = movie.characters;

    for (const movieCharacter of characterUrl) {
      request(movieCharacter, (res, error, body) => {
        if (error) {
          console.log(error);
        } else {
          const movieCharacter = JSON.parse(body);
          console.log(movieCharacter.name);
        }
      });
    }
  }
});
