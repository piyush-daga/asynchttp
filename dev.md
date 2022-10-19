[x] Make the userspace design first and then create interfaces based on that

[] Use github tasks or something similar for tracking.

[] AnyIO

[] Semaphore support

[] Backoff and retry

[] Logging Configuration for Backing off

[] Support for progress bar?

[] AsyncClient to not open connections again and 
again

[] Buffer for o/p

[] PK if dict buffer is supported

[] Structure

    [] Create a parent class for basic args
    [] Functions such as get, post etc...

[] Start soon is also abstracted from the user

[] Userspace code as simple as:
```python
with AsyncHTTPRequest() as ahttp:
    for url in urls:
        ahttp.get(url)
```
[] Maybe we can use `events` to sync?