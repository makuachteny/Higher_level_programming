#!/usr/bin/node

// The `process.argv` array contains the command line arguments passed to the Node.js script.
// The element at index `2` of the `process.argv` array represents the first command line argument passed to the script, excluding the path to node and the path to the script.

// This `if` statement checks if the element at index `2` of the `process.argv` array is `undefined`.
// If it is `undefined`, then the console will log 'No argument'.
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  // If the element at index `2` of the `process.argv` array is not `undefined`, then the code will enter this block.
  // The console will log the value of the element at index `2` of the `process.argv` array.
  console.log(process.argv[2]);
};
