var memoize = function (memo, fundamental) {
  var shell = function (n) {
    var result = memo[n];
    if (typeof result !== 'number') {
      result = fundamental(shell, n);
      memo[n] = result
    }
    return result;
  }
  return shell;
};

var fibonacci = memoize([0,1], function (shell, n) {
  return shell(n - 1) + shell(n - 2);
})

for (var i = 0; i <= 10; i += 1) {
  console.log(i + ': ' + fibonacci(i));
}

var factorial = memoize([1], function (shell, n) {
  return shell(n - 1) * n;
})

for (var i = 0; i <= 10; i += 1) {
  console.log(i + ': ' + factorial(i));
}