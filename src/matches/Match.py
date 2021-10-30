from logging import getLogger
from spacy import explain
from spacy.tokens import Doc, Span
from ..nlp import nlp
from ..patterns import Rulename


MatchId = int
Start = int
End = int
RawMatch = tuple[MatchId, Start, End]
SpanFeatures = dict[str, str]


logger = getLogger(__name__)


def extract_span_features(span: Span) -> SpanFeatures:
    """Extract useful attributes from the matching `Span`."""
    logger.debug(f"Parsing the '{span}' Span")
    return {
        "span": span,
        "phrase": span.text,
        "root": span.root.text,
        "root_head": span.root.head.text,
        "pos": span.root.pos_,
        "tag": span.root.tag_,
        "dep": span.root.dep_,
        "phrase_lemma": span.lemma_,
        "root_lemma": span.root.lemma_,
        "pos_desc": explain(span.root.pos_),  # type: ignore # explain is untyped
        "tag_desc": explain(span.root.tag_),  # type: ignore # explain is untyped
        "dep_desc": explain(span.root.dep_),  # type: ignore # explain is untyped
    }


class Match:
    """A helper class that wraps the output of the spaCy Matcher and provides useful attributes."""

    def __init__(self, raw_match: RawMatch, doc: Doc) -> None:
        (match_id, start, end) = raw_match
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
