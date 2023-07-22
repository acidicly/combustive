import multiprocessing

from .utils import export

@export
def multiprocessing_executor(args:tuple = None,name:str = None,daemon:bool = False,**kwargs):
    """
    Decorator for the multiprocessing.Process class
    :param args: The arg tuple of the wrapped function
    :param name: The Process name
    :param kwargs: The keyword arguments for the wrapped function
    :param daemon: Whether the process is a daemon one.
    :return: A multiprocessing.Process instance
    """
    def decorator(func):
        if kwargs and args:
            return multiprocessing.Process(target=func,name=name,args=args,kwargs=kwargs,daemon=daemon)
        elif kwargs:
            return multiprocessing.Process(target=func,kwargs=kwargs,daemon=daemon)
        elif args:
            return multiprocessing.Process(target=func,name=name,args=args,daemon=daemon)
        else:
            return multiprocessing.Process(target=func,name=name,daemon=daemon)
    return decorator