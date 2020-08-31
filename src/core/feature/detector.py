import logging
from warnings import warn
from spacy import explain
from src.util.spacy import make_doc, run_matcher
from .transformer import parse_phrase_features_from_chunk


class FeatureDetector:
    """The abstraction for bridging to Feature instances (implementors)."""

    logger = logging.getLogger(__name__)

    def __init__(self, feature_klass, matcher):
        self.logger.debug(f"Constructing FeatureDetector for `{feature_klass}` with matcher `{matcher}`")
        self._feature_klass = feature_klass
        self._matcher = matcher

    def determine_features(self, pattern_name, span):
        self.logger.error("determine_features() was not implemented")
        raise NotImplementedError

    def to_feature(self, pattern_name, span):
        self.logger.debug(f"Creating instance of `{self._feature_klass}`")
        feature = self._feature_klass()

        self.logger.debug(f"Extracting features from the pattern `{pattern_name}` and the span `{span}`")
        feature_dict = self.determine_features(pattern_name, span)

        self.logger.debug(f"Setting `{feature}` attributes to `{feature_dict}` attributes")
        for key in feature_dict:
            feature_dict_val = feature_dict[key]
            self.logger.debug(f"Adding `{feature_dict_val}` to `{key}`")
            setattr(feature, key, feature_dict_val)
        return feature

    def detect_many(self, maybe_tokenized):
        self.logger.debug(f"Detecting features in `{maybe_tokenized}`")
        doc = make_doc(maybe_tokenized)
        matches = []
        if self._matcher:
            self.logger.debug(f"Running the matcher on `{doc}`")
            matches = run_matcher(self._matcher, doc)
            self.logger.debug(f"The matcher found `{len(matches)}` match(es)")
        else:
            # if matcher was not provided and the input is intended to be used as
            # the span for determine_features(), create a dummy match with the 
            # input as the span and put it in a list so that the output is 
            # compatible with the to_feature() calls below
            self.logger.debug("No matcher was provided for detection")
            matches = [("", doc)]
            self.logger.debug("Set matches to the dummy")

        if not matches:
            err_msg = "No matches were found"
            self.logger.debug(err_msg)
            raise ValueError(err_msg)
        self.logger.debug(f"Creating feature instances of type `{self._feature_klass}`")
        features = [self.to_feature(name, span) for (name, span) in matches]
        self.logger.debug(f"Created `{len(features)}` instance(s)")
        return features

    def detect_one(self, maybe_tokenized):
        features = self.detect_many(maybe_tokenized)
        if len(features) > 1:
            err_msg = f"detect_one() expected one `{self._feature_klass}` but received `{len(features)}`"
            self.logger.warning(err_msg)
            warn(err_msg)
        feature = features[0]
        print(f"Returning the feature `{feature}`")
        return feature


class SimpleFeatureDetector(FeatureDetector):
    """A refined abstraction for bridging to SimpleFeature instances (implementors)."""

    def determine_features(self, pattern_name, span):
        return { "value": pattern_name }


class PhraseFeatureDetector(FeatureDetector):
    """A refined abstraction for bridging to PhraseFeature instances (implementors)."""

    def determine_features(self, pattern_name, span):
        return parse_phrase_features_from_chunk(span)
