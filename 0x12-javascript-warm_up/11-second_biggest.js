#!/usr/bin/node

const ints = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (ints.length <= 1) {
  console.log(0);
} else {
  console.log(ints.sort((a, b) => {
    return b - a;
  })[1]);
}
