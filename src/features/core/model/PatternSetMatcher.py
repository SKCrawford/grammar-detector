from spacy.tokens.doc import Doc
from spacy.matcher import Matcher
from src.nlp import nlp
from .PatternSet import PatternSet


class PatternSetMatcher:
    """An extension of the spaCy matcher.

    After passing the PatternSet instance to the constructor, the rules in that
    pattern set are automatically added to the spaCy matcher under the hood.
    """

    _is_loaded = False
    _pattern_set = None
    _matcher = Matcher(nlp.vocab)

    def __init__(self, pattern_set):
        if isinstance(pattern_set, type(nlp)):
            raise TypeError(
                "expects PatternSet instance but got nlp instance")
        if not isinstance(pattern_set, PatternSet):
            raise TypeError(
                f"expects PatternSet instance but got {type(pattern_set)}")
        self._pattern_set = pattern_set
        self._load()

    def __call__(self, doc):
        if not self._is_loaded:
            self._load()
        return self._matcher(doc)

    def _load(self):
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

        Given a doc and a list of matches, return a tuple of (rulename, span).
        """
        if not isinstance(doc, Doc):
            raise TypeError(
                f"expects Doc instance but got {type(doc)}")
        if not list or not isinstance(matches, list):
            raise TypeError(
                f"expects a list of matches but got {type(matches)}")

        best_match_rulename = ""
        best_match_span = ""

        for (match_id, start, end) in matches:
            rulename = nlp.vocab.strings[match_id]
            span = doc[start:end]

            if len(best_match_span) < len(span):
                best_match_rulename = rulename
                best_match_span = span

        return (best_match_rulename, best_match_span)
