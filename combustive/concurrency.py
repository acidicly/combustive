import threading
import asyncio

from .utils import export

@export
def run_program_forever() -> None:
    """
    Will run the program that this was called in forever.
    """
    def __int():
        while True:
            None

    threading.Thread(target=__int).start()

@export
def async_main(fn):
    """
    Run an async main function from a synchronous environment using asyncio
    """
    asyncio.run(fn())

