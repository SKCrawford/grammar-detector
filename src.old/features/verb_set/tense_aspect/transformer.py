import re


def extract_tense_aspect(verb_tense):
    """Determine the tense and aspect of a verb tense phrase. For example
    'future perfect continuous' should return ('future', 'perfect continuous').
    Irrelevant features, such as person or descriptors, are removed. For example,
    'future simple be-going-to' should return ('future', 'simple').

    Given a string, return a tuple of (string, string).
    """
    tense = ""
    aspect = ""
    reg = r"(present|past|future)\s(simple|perfect continuous|perfect|continuous)"
    match = re.match(reg, verb_tense)
    if match:
        tense = match.group(1).strip()
        aspect = match.group(2).strip()
    return (tense, aspect)
