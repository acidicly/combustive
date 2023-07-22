## Loop function wrapper

### loop()

It wraps a function and has the following time arguments:

- days:int
- hours:int
- minutes:int
- seconds:int

all of the above get summed up to provide the cycle timing or every how often does the function get triggered.

- runner:LoopRunner -> What runner is to be used Threading (LoopRunner.THREADING) or Multiprocessing (LoopRunner.MULTIPROCESSING)

Returns a  Loop class stance which has the following attributes exposed:

- cycle_seconds:int -> The seconds per cycle 
- loop_runner_type:LoopRunner -> The type of runner being used in this loop
- loop_runner:ThreadRunner | multiprocessing.Process -> The runner object itself. 
- running:bool -> If the loop is running
- on_startup:Callable -> A function that gets called just before the loop starts
- on_shutdown:Callable -> A function that gets called just after the loop ends.
- on_error:Callable -> A function that gets called if an Exception gets raised inside the loop.

and with the methods:

- start() -> Starts this loop. Raises a RuntimeException if the loop has been started already and triggers the on_startup callable.
- stop() -> Stop this loop. Raises a RuntimeException if the loop has been stopped already and triggers the on_shutdown callable.

#### Example:

```python
import time
from combustive import loop, LoopRunner

@loop(seconds=1, runner=LoopRunner.MULTIPROCESSING)
def hi():
    print("hi")

hi.on_startup = lambda: print("Started")
hi.on_shutdown = lambda: print("Stopped")

hi.start()
time.sleep(1)
print(hi.loop_runner.ident)
time.sleep(9)
hi.stop()
```
will print:

```
Started
hi
61134 (Random id)
hi
hi
hi
hi
hi
hi
hi
hi
hi
Stopped
```