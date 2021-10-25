from logging import getLogger
from spacy.tokens import Doc, Span
from ..extractors import extract_span_features, SpanFeatures
from ..nlp import nlp
from ..patterns import Rulename


MatchId = int
Start = int
End = int
SpacyMatch = tuple[MatchId, Start, End]


logger = getLogger(__name__)


class Match:
    """A helper class that wraps the output of the spaCy Matcher and provides useful attributes."""

    def __init__(self, spacy_match: SpacyMatch, doc: Doc) -> None:
        (match_id, start, end) = spacy_match
        self.match_id: MatchId = match_id
        self.start: Start = start
        self.end: End = end
        self.doc: Doc = doc

    def __repr__(self):
        return f"<{self.rulename}: {self.span}>"

    @property
    def rulename(self) -> Rulename:
        return nlp.vocab.strings[self.match_id]

    @property
    def span(self) -> Span:
        return self.doc[self.start : self.end]

    @property
    def span_features(self) -> SpanFeatures:
        return extract_span_features(self.span)
