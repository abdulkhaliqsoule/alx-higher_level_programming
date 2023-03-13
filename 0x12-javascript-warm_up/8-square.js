#!/usr/bin/node
const argv = process.argv;
const size = parseInt(argv[2]);
const character = 'X';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write(`${character}`);
    }
    console.log();
  }
}
