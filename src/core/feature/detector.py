from spacy import explain
from src.util.spacy import make_doc, run_matcher
from .transformer import parse_phrase_features_from_chunk


class FeatureDetector:
    """The abstraction for bridging to Feature instances (implementors)."""

    def __init__(self, feature_klass, matcher):
        self._feature_klass = feature_klass
        self._matcher = matcher

    def determine_features(self, pattern_name, span):
        raise NotImplementedError

    def to_feature(self, pattern_name, span):
        feature = self._feature_klass()
        feature_dict = self.determine_features(pattern_name, span)
        for key in feature_dict:
            setattr(feature, key, feature_dict[key])
        return feature

    def detect(self, maybe_tokenized):
        doc = make_doc(maybe_tokenized)
        # if matcher was not provided and the input is intended to be used as
        # the span for determine_features(), create a dummy match with the 
        # input as the span and put it in a list so that the output is 
        # compatible with to_feature()
        matches = [("", doc)] if not self._matcher else run_matcher(self._matcher, doc)
        features = [self.to_feature(name, span) for (name, span) in matches]
        return features


class SimpleFeatureDetector(FeatureDetector):
    """A refined abstraction for bridging to SimpleFeature instances (implementors)."""

    def determine_features(self, pattern_name, span):
        return { "value": pattern_name }


class PhraseFeatureDetector(FeatureDetector):
    """A refined abstraction for bridging to PhraseFeature instances (implementors)."""

    def determine_features(self, pattern_name, span):
        return parse_phrase_features_from_chunk(span)
