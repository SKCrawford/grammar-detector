from .model import SentenceFeatureSet


class SentenceFeatureSetBuilder:
    """Create and modify a SentenceFeatureSet instance."""

    _instance = None

    def spawn(self):
        """Create an instance.
        
        Given void, return self.
        """
        self._instance = SentenceFeatureSet()
        return self

    def build(self):
        """Return the instance created in spawn().
        
        Given void, reutrn a SentenceFeatureSet instance.
        """
        return self._instance

    def set_sentence(self, sentence):
        self._instance.sentence = sentence
        return self

    def set_verb_feature_set(self, verb_feature_set):
        self._instance.verb_features = verb_feature_set
        return self
