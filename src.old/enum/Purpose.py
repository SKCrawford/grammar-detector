from enum import Enum


class Purpose(Enum):
    """The most common reasons why a text is written. This is typically
    reflected in the syntax and ending punctuation. Interrogative is detected
    by (NYI) the presence of do/wh-word, auxiliary fronting, and a question
    mark. Imperative is detected by (NYI) the absence of a subject and
    the form of the verb (plain form).
    """

    DECLARATIVE = "declarative"
    INTERROGATIVE = "interrogative"
    EXCLAMATORY = "exclamatory"
    IMPERATIVE = "imperative"
    UNKNOWN = "???"
