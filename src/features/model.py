from src.util.serializable import Serializable


class FeatureSet(Serializable):
    def __init__(self):
        # the untokenized sentence
        self.sentence = ""

        # features relating to the nouns in the sentence
        self.nouns = []

        # features relating to the root verb
        self.verbs = []
