from functools import cached_property
from logging import getLogger
from spacy import explain
from spacy.tokens import Doc, Span
from ..Nlp import Nlp


MatchId = int
Start = int
End = int
RawMatch = tuple[MatchId, Start, End]
SpanFeatures = dict[str, str]


logger = getLogger(__name__)


class Match:
    """A helper class that wraps the output of the spaCy Matcher and provides useful attributes."""

    def __init__(self, raw_match: RawMatch, doc: Doc) -> None:
        logger.debug(f"Constructing the Match for '{doc.text}'")
        (match_id, start, end) = raw_match
        self.match_id: MatchId = match_id
        self.start: Start = start
        self.end: End = end
        self.doc: Doc = doc

    def __repr__(self):
        return f"<{self.rulename}: {self.span}>"

    @cached_property
    def rulename(self) -> str:
        return Nlp()._nlp.vocab.strings[self.match_id]

    @cached_property
    def span(self) -> Span:
        return self.doc[self.start : self.end]

    @cached_property
    def span_features(self) -> SpanFeatures:
        """Extract useful attributes from the matching `Span`."""
        logger.debug(f"Parsing the '{self.span}' Span")
        return {
            "span": self.span,
            "phrase": self.span.text,
            "root": self.span.root.text,
            "root_head": self.span.root.head.text,
            "pos": self.span.root.pos_,
            "tag": self.span.root.tag_,
            "dep": self.span.root.dep_,
            "phrase_lemma": self.span.lemma_,
            "root_lemma": self.span.root.lemma_,
            "pos_desc": explain(self.span.root.pos_),  # type: ignore # explain is untyped
            "tag_desc": explain(self.span.root.tag_),  # type: ignore # explain is untyped
            "dep_desc": explain(self.span.root.dep_),  # type: ignore # explain is untyped
        }
