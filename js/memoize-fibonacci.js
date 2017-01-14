// Memoized example
var callCounter = 0;

var fibonacci = function () {
  var memo = [0,1];
  var fibonacci = function (n) {
    console.log('callCounter: ' + ++callCounter)
    return memo[n] !== undefined ? memo[n] : memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
  }
  return fibonacci;
}();

for (var i = 0; i <= 10; i += 1) {
  console.log(i + ': ' + fibonacci(i));
}
