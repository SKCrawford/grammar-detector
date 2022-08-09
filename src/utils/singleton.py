from logging import getLogger
from functools import wraps


logger = getLogger(__name__)


def singleton(klass):
    instances = []

    @wraps(klass.__new__)
    def _singleton(*args, **kwargs):
        if not instances:
            logger.debug(f"Constructing a new {klass}")
            instance = klass(*args, **kwargs)
            instances.append(instance)
        else:
            logger.debug(f"Retrieving an existing {klass}")
        return instances[0]

    return _singleton
