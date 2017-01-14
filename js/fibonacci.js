// Non memoized example
var callCounter = 0;

var fibonacci = function (n) {
  console.log('callCounter: ' + ++callCounter)
  return n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2);
}

for (var i = 0; i <= 10; i += 1) {
  console.log(i + ': ' + fibonacci(i));
}
