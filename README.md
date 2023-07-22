# Combustive

A set of utilities for the python modules, [threading](https://docs.python.org/3/library/threading.html) and [multiprocessing](https://docs.python.org/3/library/multiprocessing.html).

## Example Usage

For a more detailed look at the executors (passing args,kwargs,and more) take a look at the [thread_executor](https://github.com/acidicly/combustive/blob/main/docs/threading_executor.md) or [multiprocessing_executor](https://github.com/acidicly/combustive/blob/main/docs/multiprocessing_executor.md) documentation.

### Threading
```python
import time
from combustive import thread_executor

@thread_executor() 
def test(): 
    # the code you want to run here

test.start() # Start the thread
time.sleep(10)
test.kill() # Kill it (This will throw an exception in the terminal)
```

### Multiprocessing
```python
import time
from combustive import multiprocessing_executor

@multiprocessing_executor()
def test():
    # the code you want to run here

test.start() # Start the process
time.sleep(10)
test.terminate() # Terminate the process
```

### Background Loop

Check the [documentation](https://github.com/acidicly/combustive/blob/main/docs/loop.md) of the background loop for a more detailed look at it and its arguments.

```python
import time
from combustive import loop,LoopRunner

@loop(seconds=10,runner=LoopRunner.THREADING)
def test():
    # The code you want to run every 10 seconds

test.start() # Start the background loop
time.sleep(10)
test.stop() # Stop it
```
