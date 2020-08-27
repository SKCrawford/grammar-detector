from src.core.pattern.factory import PatternSetFactory
from src.SyntaxPatterns import SyntaxPatterns


def create_noun_person_pattern_set():
    """ Return a pattern set related to noun persons.

    Given void, return a PatternSet instance.
    """
    return PatternSetFactory()      \
        .set_json_key("persons")    \
        .set_name("person")         \
        .build()                    \
