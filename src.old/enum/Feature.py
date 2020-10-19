from enum import Enum


class Feature(Enum):
    """All supported linguistic features in a FeatureSet instance."""

    SENTENCE = "sentence"
    SUBJECT = "subject"
    VERB = "verb"
    OBJECT = "object"
    TENSE = "tense"
    ASPECT = "aspect"
    IS_THIRD_PERSON = "is_third_person"
    VOICE = "voice"
    PURPOSE = "purpose"
    NAMES = "names"
    ENDING_PUNCT = "ending_punct"
