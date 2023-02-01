#!/usr/bin/node

// The process.arg array contains the command line arguments passed to the Node.js scripy
// The '?' is a ternary operator that checks the undefined value of process.argv

console.log(process.arg.slice[2] === undefined ? 'No argument' : process.arg[2])

