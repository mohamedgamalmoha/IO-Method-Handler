import io
import sys
import time
from typing import IO, Any, Callable


class IOHandler:
    """Input/Output Handler deals with methods that have IO call and needs a test in auto way"""

    def __init__(self, method: Callable, handler: io.IOBase = io.StringIO) -> None:
        self.method = method
        self.handler = handler
        self.orig_stdin = None

    def __call__(self, txt_inp: str, *args, **kwargs) -> Any:
        """Calling the method with args & kwargs"""
        self.setup_method()
        results = self.test_method(txt_inp, *args, **kwargs)
        self.teardown_method()
        return results

    def input_handler(self, txt_inp: str) -> IO:
        """Get handler with text input"""
        return self.handler(txt_inp)

    def test_method(self, txt_inp: str, *args, **kwargs) -> Any:
        """Run the method with io handler"""
        # Assign the handler as original input
        sys.stdin = self.input_handler(txt_inp)
        return self.method(*args, **kwargs)

    def setup_method(self) -> None:
        """Setup needs for running the method"""
        # Save the original input
        self.orig_stdin = sys.stdin

    def teardown_method(self) -> None:
        """Undo all changes made in setup method"""
        # Re-assign the original input
        sys.stdin = self.orig_stdin


class TimerMixin:
    """Calculate the time of calling the method"""
    start_time: float
    end_time: float

    def setup_method(self) -> None:
        super().setup_method()
        self.start_time = time.perf_counter()

    def teardown_method(self) -> None:
        self.end_time = time.perf_counter()
        super().teardown_method()

    @property
    def total_time(self):
        return self.end_time - self.start_time


class CounterMixin:
    """Count the number ot calling the method"""

    counter: int = 0
    
    def __call__(self, txt_inp: str, *args, **kwargs) -> Any:
        self.counter += 1
        return super().__call__(txt_inp,  *args, **kwargs)


class TimedIOHandler(TimerMixin, IOHandler):
    """IOHandler with a timer"""


class CountedIOHandler(CounterMixin, IOHandler):
    """IOHandler with counter"""


class TimedCountedIOHandler(TimerMixin, CounterMixin, IOHandler):
    """IOHandler with both timer and counter"""
