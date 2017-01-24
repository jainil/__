# Benefits (practical) of `"use strict"`

- debugging is easier; noisier errors
- prevents accidental globals: assigning to udeclared variables throws an error
- eliminates `this` coercion to the global (when `this` is undefined)
- disallows duplicate property names as parameter values
- makes `eval()` safer: vars and functions not created in containing scope
- throws error on invalid usage of `delete`
