#!/usr/bin/node

const fs = require('fs');

// Function to handle errors and exit the script
function handleError (error) {
  console.error('Error:', error);
  process.exit(1); // Exit with an error code
}

// Check for missing arguments
if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <fileA> <fileB> <outputFile>');
  process.exit(1); // Exit with an error code
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const outputFilePath = process.argv[4];

// Asynchronous reading and writing using Promises
Promise.all([
  // Read file A content
  new Promise((resolve, reject) => {
    fs.readFile(fileAPath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  }),
  // Read file B content
  new Promise((resolve, reject) => {
    fs.readFile(fileBPath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  })
])
  .then(([fileAContent, fileBContent]) => {
  // Combine content with a newline separator
    const combinedContent = `${fileAContent}\n${fileBContent}`;

    // Write combined content to the output file
    return new Promise((resolve, reject) => {
      fs.writeFile(outputFilePath, combinedContent, 'utf8', (err) => {
        if (err) {
          reject(err);
        } else {
          resolve();
        }
      });
    });
  })
  .then(() => {
    console.log('Successfully wrote combined file');
  })
  .catch(handleError); // Catch any errors and handle them
