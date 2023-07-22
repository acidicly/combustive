## Concurrency
This module holds:

- async_main -> function decorator
- run_program_forever -> function

### - async_main decorator

It runs an async main like a normal main() using asyncio.run()

```python
from combustive import async_main

@async_main
async def hello():
    print("hi")
```

will print

```
hi
```

### - run_program_forever function

Will run the current program forever (even if there are no other non daemon processes running on the program). It does this by spawning a non daemon thread that does nothing.


```python
from combustive import run_program_forever,thread_executor

run_program_forever()

@thread_executor(daemon=True)
async def hello():
    print("hi")

hello.start()
```
will print
```
hi
``` 
without the program terminating.