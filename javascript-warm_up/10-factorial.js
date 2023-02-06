#!/usr/bin/node
function factoriale (number) {
  if (number < 1) {
    return 1;
  }
  return number * factoriale(number - 1);
}
if (isNaN(process.argv[2])) {
  console.log(1);
} else console.log(factoriale(Number(process.argv[2])));
