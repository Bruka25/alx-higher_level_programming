#!/usr/bin/node

const convertInt = parseInt(process.argv[2]);

if (!isNaN(convertInt)) {
  console.log('My number:', convertInt);
} else {
  console.log('Not a number');
}
