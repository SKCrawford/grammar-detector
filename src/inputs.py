from spacy.tokens import Doc, Span
from .nlp import nlp


class Input:
    def __init__(self, raw_input: str) -> None:
        self.raw: str = raw_input
        self.doc: Doc = nlp(raw_input)

    @property
    def docs(self) -> list[Doc]:
        return [self.doc]

    @property
    def noun_chunks(self) -> list[Span]:
        return self.doc.noun_chunks
