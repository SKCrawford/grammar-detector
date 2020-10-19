import logging


logger = logging.getLogger(__name__)


class Builder:
    def __init__(self, klass):
        logger.debug(f"Constructing builder for `{klass}`")
        self._klass = klass
        self._instance = None

    def _ensure_spawned(self):
        if not self._instance:
            self.spawn()

    def spawn(self, *args, **kwargs):
        """Create the private instance. Pass the args and kwargs to the
        klass' constructor.

        Given args and/or kwargs, return self.
        """
        logger.debug(f"Spawning instance of `{self._klass}`")
        self._instance = self._klass(*args, **kwargs)
        return self

    def set_attr(self, name, value):
        """Set the verb to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        logger.debug(f"Setting instance's attribute `{name}` to `{value}`")
        if not hasattr(self._instance, name):
            msg = f"Invalid attribute name `{name}`"
            logger.error(msg)
            raise ValueError(msg)
        setattr(self._instance, name, value)
        return self

    def build(self):
        """Finalize the creation of the VerbFeatureSet.

        Given void, return a VerbFeatureSet instance.
        """
        self._ensure_spawned()
        logger.debug(f"Returning the instance `{self._instance}`")
        return self._instance
