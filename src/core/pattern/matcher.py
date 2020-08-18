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

    def best_match(self, doc, matches):
        """Determine the best match out of a list of matches.

        The best match is determined by the length of the matches' `span`s.
        Some verb tenses will be flagged for multiple matches. For example,
        'I will have been doing that' will be flagged for both:
            * present perfect continuous 'have been doing'
            * future perfect continuous 'will have been doing'
        The length of 'will have been doing' is longer than 'have been doing',
        so the best match will be the longer span. This method should
        not be necessary if the patterns are well-made.

        Given a Doc instance and a list of Match instances, return a tuple of (string, string).
        """
        is_type(doc, Doc)
        is_type(matches, list)
        is_truthy(matches)

        best_match_rulename = ""
        best_match_span = ""

        for (match_id, start, end) in matches:
            rulename = nlp.vocab.strings[match_id]
            span = doc[start:end]

            if len(best_match_span) < len(span):
                best_match_rulename = rulename
                best_match_span = span

        return (best_match_rulename, best_match_span)
