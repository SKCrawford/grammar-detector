import json
from src.util.serializable import Serializable


class SentenceFeatureSet(Serializable):
    """A dictionary of the linguistic features of a sentence. The sentence
    itself is also exposed. This is intended to be used in conjunction
    with the SentenceFeatureSetBuilder to create and modify instances.
    It is not intended to call the constructor manually.
    """

    def __init__(self):
        # the untokenized sentence
        self.sentence = ""

        # features relating to the nouns in the sentence
        self.noun_features = None

        # features relating to the root verb
        self.verb_features = None
