#!/usr/bin/node
function factorial (n) {
  if ((Number.isNaN(n)) || (n === 1)) {
    return 1;
  }
  return factorial(n - 1) * n;
}

console.log(factorial(parseInt(process.argv[2])));
