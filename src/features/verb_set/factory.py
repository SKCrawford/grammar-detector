from src.util.transformer import remove_ordinals, split_words_into_first_and_rest
from .model import VerbFeatureSet


unknown_text_default = "???"


class VerbFeatureSetFactory:
    """Creates VerbFeatureSet instances from a Match instance."""

    _instance = None
    _match = None
    _unknown_text = ""

    def __init__(self, match, unknown_text=unknown_text_default):
        """Given a Match instance and optional kwarg unknown_text, construct an instance."""
        self._match = match
        self._unknown_text = unknown_text

    def _spawn(self):
        self._instance = VerbFeatureSet()

    def _extract_verb_and_tense(self):
        """Returns a tuple of (verb, verb_tense). Note the difference between
        verb_tense, tense, and aspect. Here's an example:
        verb_tense = "future perfect continuous"
        tense = "future"
        aspect = "perfect continuous"

        Given void, returns a tuple of (string, string).
        """
        if not self._instance:
            raise ValueError("call _spawn() first")

        verb = self._unknown_text
        (verb_tense, verb_span) = self._match
        if verb_span and verb_span.text:
            verb = verb_span.text
        return (verb, verb_tense)


    def build(self):
        """Create a VerbFeatureSet instance. Break apart the match and
        extract the verb's features.

        Given void, return a VerbFeatureSet instance.
        """
        self._spawn()
        (verb, verb_tense) = self._extract_verb_and_tense()
        (tense, aspect) = split_words_into_first_and_rest(verb_tense)

        self._instance.verb = verb
        self._instance.tense = tense
        self._instance.aspect = aspect
        return self._instance
