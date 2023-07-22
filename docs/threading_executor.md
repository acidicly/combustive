## Thread Executor function wrapper

### @thread_executor()
It wraps a function and has the following arguments:

- args:tuple -> A tuple containing the arguments to the wrapped function.
- name:str -> Your custom name for the thread that is going to run this function.
- kwargs -> The function's key word arguments.
- daemon:bool -> Whether the thread that is going to run this function is a daemon one or not.

returns a ThreadRunner object.

#### Examples:

- Basic **args** and **kwargs** usage

```python
import time
from combustive import thread_executor

@thread_executor(args=("acidicly",))
def test(username: str):
    print(f"Hi {username}")

@thread_executor(username="acidicly") 
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

- You can also kill a thread by calling its .kill() method:

```python
import time
from combustive import thread_executor

@thread_executor()
def test():
    #code here

test.start()
time.sleep(1)
test.kill()
```

this will raise an error to kill the thread.

- You can also get the internal thread object and access its methods as well:

```python
import time
from combustive import thread_executor

@thread_executor()
def test():
    #code here

print(test.thread.ident)
```
