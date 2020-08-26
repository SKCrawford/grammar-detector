class Builder:
    def __init__(self, klass):
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
        self._instance = self._klass(*args, **kwargs)
        return self

    def set_attr(self, name, value):
        """Set the verb to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        if not hasattr(self._instance, name):
            raise ValueError(f"invalid attribute {name}")
        setattr(self._instance, name, value)
        return self

    def build(self):
        """Finalize the creation of the VerbFeatureSet.

        Given void, return a VerbFeatureSet instance.
        """
        self._ensure_spawned()
        return self._instance
