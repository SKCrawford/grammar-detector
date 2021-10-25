from logging import getLogger
from spacy.tokens import Doc, Span
from ..nlp import nlp
from ..patterns import Rulename
from ..extractors import extract_span_features, SpanFeatures


MatchId = int
Start = int
End = int
SpacyMatch = tuple[MatchId, Start, End]


logger = getLogger(__name__)


class Match:
    def __init__(self, spacy_match: SpacyMatch, doc: Doc) -> None:
        self.match_id: MatchId = match_id
        self.start: Start = start
        self.end: End = end
        self.doc: Doc = doc

    @property
    def rulename(self) -> Rulename:
        return nlp.vocab.strings[self.match_id]

    @property
    def span(self) -> Span:
        return self.doc[self.start : self.end]

    def span_features(self) -> SpanFeatures:
        return extract_span_features(self.span)
