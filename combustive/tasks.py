import enum
import time
import typing
import multiprocessing

from .threading import ThreadRunner,_StopThread
from .utils import export

@export
class LoopRunner(enum.Enum):
    THREADING = 1
    MULTIPROCESSING = 2

class LoopClass:
    def __init__(
            self,
            call: typing.Callable,
            days: int,
            hours: int,
            minutes: int,
            seconds: int,
            runner: LoopRunner
    ):
        """
        The internal loop function
        :param call: The loop callback
        :param days: The amount of days to be used in the cycle
        :param hours: The amount of hours to be used in the cycle
        :param minutes: The amount of minutes to be used in the cycle
        :param seconds: The amount of seconds to be used in the cycle
        :param runner: What type of runner to be used CustomThread or Multiprocessing
        """
        self._callback = call  # The callback or the thing that gets executed when the loop ends
        self._execute_on_startup: typing.Callable = None  # The function that gets called ONCE just before the loop starts
        self._execute_on_shutdown: typing.Callable = None  # The function that gets called ONCE as the loop stops
        self._execute_on_error: typing.Callable = None  # The function that gets called when an error occurs inside the loop


        self.cycle_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds  # Cycle seconds
        self.loop_runner_type = runner # Type of runner we are using
        self.loop_runner: ThreadRunner | multiprocessing.Process = None # Our internal runner obj
        self.running: bool = False # If the loop is running

    @property
    def on_startup(self):
        return self._execute_on_startup

    @on_startup.setter
    def on_startup(self, call: typing.Callable):
        self._execute_on_startup = call

    @property
    def on_shutdown(self):
        return self._execute_on_shutdown

    @on_shutdown.setter
    def on_shutdown(self, call: typing.Callable):
        self._execute_on_shutdown = call

    @property
    def on_error(self):
        return self._execute_on_error

    @on_error.setter
    def on_error(self, call: typing.Callable):
        self._execute_on_error = call

    def start(self):
        if self.running:
            raise RuntimeError("The task has already been started.")

        if self.loop_runner_type == LoopRunner.THREADING:
            self.loop_runner = ThreadRunner(fn=self._loop,daemon=True)
        else:
            self.loop_runner = multiprocessing.Process(target=self._loop,daemon=True)

        if self._execute_on_startup:
            self._execute_on_startup()
        self.loop_runner.start()
        self.running = True

    def stop(self):
        if not self.running:
            raise RuntimeError("The task has not been started.")

        if self.loop_runner_type == LoopRunner.THREADING:
            self.loop_runner.kill()
        else:
            self.loop_runner.terminate()

        if self._execute_on_shutdown:
            self._execute_on_shutdown()
        self.running = False

    def _loop(self):
        while True:
            try:
                self._callback()
            except:
                if self._execute_on_error:
                    self._execute_on_error()
            time.sleep(self.cycle_seconds)

@export
def loop(runner: LoopRunner, days:int = 0, hours:int = 0, minutes:int = 0, seconds:int = 0):
    """
    Decorator for the internal loop class
    :param runner: What type of runner to be used CustomThread or Multiprocessing
    :param days: The amount of days to be used in the cycle
    :param hours: The amount of hours to be used in the cycle
    :param minutes: The amount of minutes to be used in the cycle
    :param seconds: The amount of seconds to be used in the cycle
    """

    def decorator(func):
        return LoopClass(
            call=func,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            runner=runner
        )

    return decorator