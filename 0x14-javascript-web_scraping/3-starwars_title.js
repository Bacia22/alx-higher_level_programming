#!/usr/bin/node

const req = require('request')
const url = 'https://swap-api.alx-tools.com/api/films/:id';
const id = process.argv[2]
req.get(url +id, function (error, res, body) {
if (error) {
console.log(error);
} else {
console.log(JSON.parse(body.title0;
}
});
