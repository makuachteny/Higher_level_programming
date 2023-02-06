#!/usr/bin/node

const array = process.argv.slice(2);
if (array.length === 0) console.log('No argument');
else if (array.length > 1) console.log('Arguments found');
else if (array.length === 1) console.log('Argument found');
