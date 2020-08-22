from src.util.transformer import remove_ordinals, split_words_into_first_and_rest
from .model import VerbFeatureSet


class VerbFeatureSetBuilder:
    """Creates VerbFeatureSet instances."""

    _instance = None

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
        if not self._instance:
            raise ValueError("call spawn() first")
        self._instance.verb = verb
        return self

    def derive_tense_and_aspect(self, verb_tense):
        """Determine the tense and aspect from the verb tense phrase and 
        set them to the private instance.

        Given a string, return self.
        """
        if not self._instance:
            raise ValueError("call spawn() first")
        (tense, aspect) = split_words_into_first_and_rest(verb_tense)
        self._instance.tense = tense
        self._instance.aspect = aspect
        return self

    def build(self):
        """Finalize the creation of the VerbFeatureSet.

        Given void, return a VerbFeatureSet instance.
        """
        if not self._instance:
            raise ValueError("call spawn() first")
        return self._instance
