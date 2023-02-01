#!/usr/bin/node
if (process.arg.length <= 1) {
  console.log('No argument');
} else if (process.argv.length === 1) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
