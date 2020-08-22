from spacy.matcher import Matcher
from spacy.tokens.doc import Doc
from src.nlp import nlp
from src.util.validator import is_truthy, is_type
from .model import PatternSet


class PatternSetMatcher:
    """An extension of the spaCy matcher.

    After passing the PatternSet instance to the constructor, the rules in that
    pattern set are automatically added to the spaCy matcher under the hood.
    """

    _is_loaded = False
    _pattern_set = None
    _matcher = Matcher(nlp.vocab)

    def __init__(self, pattern_set):
        is_type(pattern_set, PatternSet)
        self._pattern_set = pattern_set
        self._load()

    def __call__(self, doc):
        if not self._is_loaded:
            self._load()
        return self._matcher(doc)

    def _load(self):
        """Load the patterns in the pattern set into the matcher.
        
        Given void, return void.
        """
        for pattern in self._pattern_set.find_all():
            self._matcher.add(pattern.name, [pattern.tokens])
        self._is_loaded = True
