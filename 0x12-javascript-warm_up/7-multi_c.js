#!/usr/bin/node
const argTimes = parseInt(process.argv[2]);
if (!isNaN(argTimes)) {
  for (let i = 0; i < argTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
