from logging import getLogger
from time import time
from typing import Callable, Literal
from .singleton import singleton


logger = getLogger(__name__)


SortKeys = Literal["elapsed", "name", "started_at", "stopped_at"]


class Timer:
    def __init__(self, name: str, verbose: bool = False) -> None:
        """Create an instance of the `Timer`. Setting the timer to verbose tends to spam logs.

        Arguments:
        name -- (str) The name of the timer as seen when calling Timekeeper.report()

        Keyword arguments:
        verbose -- (bool) If True, the timer will log when it starts and stops
        """
        self._name: str = name
        self._started_at: float = 0
        self._stopped_at: float = 0
        self._verbose = verbose

    @property
    def elapsed(self) -> float:
        """Return the elapsed duration in milliseconds."""
        if not self.stopped_at:
            msg = f"Timer '{self.name}' was not stopped"
            logger.error(msg)
            raise AttributeError(msg)
        return (self.stopped_at - self.started_at) * 1000

    @property
    def name(self) -> str:
        return self._name

    @property
    def started_at(self) -> float:
        return self._started_at

    @property
    def stopped_at(self) -> float:
        return self._stopped_at

    def start(self) -> None:
        self._started_at = time()
        if self._verbose:
            logger.info(f"Timer '{self.name}' started")

    def stop(self) -> None:
        if not self._started_at:
            msg = f"Timer '{self.name}' was not started"
            logger.error(msg)
            raise AttributeError(msg)
        self._stopped_at = time()
        if self._verbose:
            logger.info(f"Timer '{self.name}' stopped")


@singleton
class Timekeeper:
    """A utility class for managing a multitude of timers."""

    def __init__(self, verbose: bool = False) -> None:
        """Create an instance of the `Timekeeper`.

        Keyword arguments:
        verbose -- (bool) If True, all Timers will log when they start and stop
        """
        self.timers: list[Timer] = []
        self.verbose: bool = verbose

    def start(self, name: str) -> Callable:
        """Return a Callable function that stops the associated Timer.

        Arguments:
        name -- (str) The name to assign to the Timer
        """
        timer = Timer(name, verbose=self.verbose)
        self.timers.append(timer)
        timer.start()
        return timer.stop

    def report(self, sort_by: SortKeys = "started_at", ascending: bool = True) -> None:
        """Print the elapsed duration of all timers in milliseconds, ordered by `sort_by`.

        Keyword arguments:
        sort_by     -- (str) One of these: elapsed, name, started_at, stopped_at
        ascending   -- (bool) If True, use ascending order. Otherwise, use descending order
        """
        key_fn: Callable[[Timer], float] = lambda t: getattr(t, sort_by)
        sorted_timers = sorted(self.timers, key=key_fn, reverse=not ascending)

        print()
        print(f"Runtimes in ms (sort_by={sort_by}, ascending={str(ascending)}):")
        for timer in sorted_timers:
            print(f"  {timer.elapsed:7.2f}: {timer.name}")
        print()


class Timeable:
    def __init__(self):
        self.tk = Timekeeper()
