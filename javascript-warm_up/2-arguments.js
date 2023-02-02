#!/usr/bin/node

// The `process.argv` array contains the command line arguments passed to the Node.js script.
// The `slice` method is used to extract a section of the array.
// Here, `2` is used as the start index, so the first two elements of the `process.argv` array (the path to node and the path to the script) are skipped.
const array = process.argv.slice(2);

// This `if` statement checks the length of the `array` variable.
// If it's equal to 0, then the console will log 'No argument'.
if (array.length === 0) console.log('No argument');

// If the length of the `array` is greater than 1, then the console will log 'Arguments found'.
else if (array.length > 1) console.log('Arguments found');

// If the length of the `array` is equal to 1, then the console will log 'Argument found'.
else if (array.length === 1) console.log('Argument found');
