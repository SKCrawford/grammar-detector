import logging


class Builder:
    def __init__(self, klass):
        logger = logging.getLogger(self.__init__.__name__)
        logger.debug(f"Started constructing builder for class `{klass}`")
        self._klass = klass
        self._instance = None
        logger.debug("Finished constructing builder")

    def _ensure_spawned(self):
        if not self._instance:
            self.spawn()

    def spawn(self, *args, **kwargs):
        """Create the private instance. Pass the args and kwargs to the
        klass' constructor.

        Given args and/or kwargs, return self.
        """
        logger = logging.getLogger(self.spawn.__name__)
        logger.debug(f"Started spawning instance of `{self._klass}`")
        self._instance = self._klass(*args, **kwargs)
        logger.debug(f"Finished spawning instance: `{self._instance}`")
        return self

    def set_attr(self, name, value):
        """Set the verb to the private instance.

        Given a string, return self.
        """
        logger = logging.getLogger(self.set_attr.__name__)
        self._ensure_spawned()
        logger.debug(f"Started setting feature value `{value}` to attribute `{name}` onto the instance `{self._instance}`")
        if not hasattr(self._instance, name):
            msg = f"Invalid attribute name `{name}`"
            logger.error(msg)
            raise ValueError(msg)
        setattr(self._instance, name, value)
        logger.debug("Finished setting feature value onto the instance")
        return self

    def build(self):
        """Finalize the creation of the VerbFeatureSet.

        Given void, return a VerbFeatureSet instance.
        """
        logger = logging.getLogger(self.build.__name__)
        self._ensure_spawned()
        logger.debug(f"Returning the built instance of class `{self._klass}`: `{self._instance}`")
        return self._instance
