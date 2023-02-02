#!/usr/bin/node

const list = process.argv.slice(2);
const array = list.map((element) => parseInt(element));
if (array.length <= 1) {
  console.log(0);
} else {
  array.sort((a, b) => {
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
  });
  console.log(array[array.length - 2]);
}
