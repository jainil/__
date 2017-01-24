# JSONP

- cross-domain requests banned except in script tags
- but nothing can be "done" on the page with the results
- when a request is made to a server with JSONP enabled, a special parameter tells the server a bit about the page, which can set up the response in such a way that the page can handle it


```
http://example.com/sample.aspx?callback=mycallback

without JSONP it return
{foo: 'bar'}

with JSONP
myCallback({foo:'bar'})
```

- no 'nice-way' to get error codes
- CORS is recommended