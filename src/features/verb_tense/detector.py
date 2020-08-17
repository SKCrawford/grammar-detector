import re
from src.nlp import nlp
from ..core.model.PatternSetMatcher import PatternSetMatcher
from .pattern_set import verb_tense_pattern_set


tense_aspect_reg = r"(\w+)\s([\w\s]*)"
verb_person_reg = r"\b(?:1st|2nd|3rd|first|second|third)"


def _strip_person(verb_tense):
    """Remove persons from the end of a verb tense, such as 1st or first."""

    return re.sub(verb_person_reg, "", verb_tense).strip()


def segment_verb_tense(verb_tense):
    """Split a verb tense into its tense and aspect.
    
    Given a string, return a tuple of (tense, aspect).
    """

    tense = "???"
    aspect = "???"

    personless_verb_tense = _strip_person(verb_tense)
    match = re.search(tense_aspect_reg, personless_verb_tense)
    if match:
        tense = match.group(1).strip()
        aspect = match.group(2).strip()
    return (tense, aspect)


def detect_verb_features(sentence):
    """Detect a sentence's tense, aspect, and verb.

    Given a string, return a tuple of (tense, aspect, verb).
    """

    if not isinstance(sentence, str):
        raise TypeError("arg[0] is not a string")

    if not sentence:
        raise ValueError("arg[0] is not truthy")

    doc = nlp(sentence)
    matcher = PatternSetMatcher(verb_tense_pattern_set)
    matches = matcher(doc)

    if not matches:
        return None

    (verb_tense, verb_span) = matcher.best_match(doc, matches)
    (tense, aspect) = segment_verb_tense(verb_tense)
    verb = verb_span.text
    return (tense, aspect, verb)
