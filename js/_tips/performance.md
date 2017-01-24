# Performance tips

## Critical rendering path

DOM, CSSOM, JS → render tree → layout → paint

render blocking CSS - blocks both JS execution and DOM construction

js is parser blocking - it blocks DOM construction
  - defer, async
  - inject the script link tag when the browser fires `DOMContentLoaded`

- minimize bytes (minify, compress, cache)
- minimize critical resources
- minimize CRP length

14kb - what one roundtrip to the server to the server fetches