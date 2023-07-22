## Multiprocessing executor function wrapper

### @multiprocessing_executor()
It wraps a function and has the following arguments:

- args:tuple -> A tuple containing the arguments to the wrapped function.
- name:str -> Your custom name for the process that is going to run this function.
- kwargs -> The function's key word arguments.
- daemon:bool -> Whether the process that is going to run this function is a daemon one or not.

returns a multiprocessing.Process object.

#### Examples:

- Basic **args** and **kwargs** usage

```python
import time
from combustive import multiprocessing_executor

@multiprocessing_executor(args=("acidicly",))
def test(username: str):
    print(f"Hi {username}")

@multiprocessing_executor(username="acidicly") 
def test2(username:str): 
    print(f"Hi {username}")
    
test.start()
test2.start()
time.sleep(1)
```
will print 
```
Hi acidicly
Hi acidicly
```

and since it returns the multiprocessing.Process instance you can access its methods and attributes directly.