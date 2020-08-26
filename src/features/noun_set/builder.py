from .model import NounFeatureSet


class NounFeatureSetBuilder:
    """Creates NounFeatureSet instances."""

    def __init__(self):
        self._instance = None

    def _ensure_spawned(self):
        if not self._instance:
            raise ValueError("call spawn() first")

    def spawn(self):
        """Create the private instance.

        Given void, return self.
        """
        self._instance = NounFeatureSet()
        return self

    def set_attr(self, name, value):
        """Set the noun to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        if not hasattr(self._instance, name):
            raise ValueError(f"invalid attribute name {name}")
        setattr(self._instance, name, value)
        return self

    def build(self):
        """Finalize the creation of the NounFeatureSet.

        Given void, return a NounFeatureSet instance.
        """
        self._ensure_spawned()
        return self._instance
