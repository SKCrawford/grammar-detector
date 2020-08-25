from .model import VerbFeatureSet


class VerbFeatureSetBuilder:
    """Creates VerbFeatureSet instances."""

    _instance = None

    def _ensure_spawned(self):
        if not self._instance:
            raise ValueError("call spawn() first")

    def spawn(self):
        """Create the private instance.

        Given void, return self.
        """
        self._instance = VerbFeatureSet()
        return self

    def set_verb(self, verb):
        """Set the verb to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        self._instance.verb = verb
        return self

    def set_tense(self, tense):
        """Set the tense to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        self._instance.tense = tense
        return self

    def set_aspect(self, aspect):
        """Set the aspect to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        self._instance.aspect = aspect
        return self

    def set_voice(self, voice):
        """Set the voice to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        self._instance.voice = voice
        return self

    def set_person(self, person):
        """Set the person to the private instance.

        Given a string, return self.
        """
        self._ensure_spawned()
        self._instance.person = person
        return self

    def build(self):
        """Finalize the creation of the VerbFeatureSet.

        Given void, return a VerbFeatureSet instance.
        """
        self._ensure_spawned()
        return self._instance
