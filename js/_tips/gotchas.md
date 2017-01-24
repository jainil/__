# Gotchas

- `delete` only deletes object properties, not variables
```js
(function(x){
  delete x;
  returns x;
})(1); // return 1
```

- keep track of `this`
```js
var foo = {
  bar: function () { return this.baz},
  baz: 1
}
typeof (f = foo.bar)(); // "undefined"
```

- isInteger(x)
  - `x^0 === x`
  - `Math.round(x) === x` or `ceil`/`floor`
  - `x%1 === 0`
  - `parseInt(x, 10) === x` - DOES NOT WORK, because parseInt first coerces `x` into a string which may change the output to scientific notation for larger numbers, failing the test.

- how execution contexts, variable objects, activation objects, and the internal "scope" property contribute to the closure behavior

- variable in closure (in for loops etc)
  - create new scope by wrapping with an IIFE that gets the current value of the variable passed
  - use foreach

- String conversion puzzles
```js
1 + "2" + "2" // "122"
1 + +"2" + "2" // "32"

"A" - "B" + "2" // "NaN2"
"A" - "B" + 2 // NaN
```

- `Array.prototype.reverse` is inplace

- Avoiding stack overflow with some recursive calls:
```js
var list = readHugeList();
var nextListItem = function () {
  var item = list.pop();
  if (item) {
    nextListItem(); // this may cause stackoverflow with very large lists
  }
}
```
This can be avoided by using `setTimeout(nextListItem, 0)`, which puts the next call on the *event queue* instead of the call stack.

- When setting an object property, js will implicitly stringify the parameter value
```js
var a = {};
var b = {key: 'b'};

a[b] = 123; // does not throw an error

// the object now looks like this:
a = {
  "[Object object]": 123
}
```

- `var a = 1 && 2` => `a = 2`. Like `||` operator `&&` returns the expression if it is evaluated to `true`.

- In event listeners:
```js
event.preventDefault() // stops the browser from executing the default action related to the event
event.stopImmediatePropagation() // stops the event from bubbling up

return false // does both of the above
```