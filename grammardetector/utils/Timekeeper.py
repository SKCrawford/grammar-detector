from logging import getLogger
from time import time
from typing import TypedDict
from .singleton import singleton


logger = getLogger(__name__)


class Record(TypedDict):
    elapsed: float
    startedAt: float
    stoppedAt: float


@singleton
class Timekeeper:
    def __init__(self) -> None:
        self._records: dict[str, Record] = {}

    def start(self, name: str) -> None:
        logger.info(f"Timekeeper start: {name}")
        self._records[name] = {
            "startedAt": time(),
            "stoppedAt": 0,
            "elapsed": 0,
        }

    def stop(self, name: str) -> None:
        logger.info(f"Timekeeper stop: {name}")
        record: Record = self._records[name]
        if not record["startedAt"]:
            raise AttributeError(f"Timekeeper entry '{name}' was not started")

        record["stoppedAt"] = time()
        record["elapsed"] = record["stoppedAt"] - record["startedAt"]

    def report(self) -> None:
        logger.info("Runtimes:")
        for name in self._records:
            record: Record = self._records[name]
            if not record["elapsed"]:
                raise AttributeError(f"Timekeeper entry '{name}' was not stopped")
            logger.info(f"  {name}: {record['elapsed']:.2f}s")
