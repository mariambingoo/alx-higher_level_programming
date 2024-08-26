#!/usr/bin/node
// returns second biggest number

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).map(Number).sort((a, b) => a - b);
  console.log(arr.reverse()[1]);
}
