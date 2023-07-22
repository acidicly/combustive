import threading
import typing
import sys

from .utils import export

class _StopThread(Exception):
    pass

# https://stackoverflow.com/a/25670684 to the rescue!
class _Thread(threading.Thread):
    """
    Custom thread object that allows for a stop mechanic to be implemented, raises a _StopThread exception when it is ready to kill the thread.
    """
    def _bootstrap(self, stop_thread=False):
        def stop():
            nonlocal stop_thread
            stop_thread = True
        self.stop = stop

        def tracer(*_):
            if stop_thread:
                raise _StopThread(f"{threading.current_thread().name} stopped.")
            return tracer
        sys.settrace(tracer)
        super()._bootstrap() # type: ignore

@export
class ThreadRunner:
    def __init__(self,fn:typing.Callable,args:tuple = None, name:str = None, kwargs:dict = None,*,daemon:bool = False):
        """
        Thread Runner, a custom Thread managing class
        :param fn: The callable non coroutine function
        :param args: The arg tuple of said function
        :param name: The thread name
        :param kwargs: The keyword arguments for the callable function
        :param daemon: Whether the thread is a daemon one.
        """
        if kwargs and args:
            self.thread = _Thread(target=fn,name=name,args=args,kwargs=kwargs,daemon=daemon)
        elif kwargs:
            self.thread = _Thread(target=fn,name=name,kwargs=kwargs,daemon=daemon)
        elif args:
            self.thread = _Thread(target=fn,name=name,args=args,daemon=daemon)
        else:
            self.thread = _Thread(target=fn,name=name,daemon=daemon)


    def start(self):
        self.thread.start()

    def kill(self):
        self.thread.stop()


    def restart(self):
        if self.thread.is_alive():
            self.kill()
            self.start()
        else:
            self.start()

    def is_running(self):
        return self.thread.is_alive()

@export
def thread_executor(args:tuple = None,name:str = None,daemon:bool = False,**kwargs):
    """
    Decorator for the ThreadRunner class
    :param args: The arg tuple of the wrapped function
    :param name: The thread name
    :param kwargs: The keyword arguments for the wrapped function
    :param daemon: Whether the thread is a daemon one.
    :return: A ThreadRunner instance creator
    """
    def decorator(func):
        return ThreadRunner(func,args,name,kwargs,daemon=daemon)

    return decorator