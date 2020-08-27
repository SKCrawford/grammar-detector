from src.util.spacy import run_matcher


class FeatureDetector:
    """The abstraction for bridging to Feature instances (implementors)."""

    def __init__(self, feature, matcher, validate_fn):
        self._feature = feature
        self._matcher = matcher
        self._validate = validate_fn

    def _get_match(self, sentence_or_doc):
        match = run_matcher(self._matcher, sentence_or_doc)
        if not match:
            return None
        (pattern_name, matching_span) = match
        return (pattern_name, matching_span)

    def set_feature(self, value):
        raise NotImplementedError

    def detect(self, sentence_or_doc):
        raise NotImplementedError


class SimpleFeatureDetector(FeatureDetector):
    """A refined abstraction for bridging to Feature instances (implementors)."""

    def set_feature(self, value):
        self._feature.value = value

    def detect(self, sentence_or_doc):
        (value, span) = self._get_match(sentence_or_doc)
        self._validate(value)
        self.set_feature(value)
        return self._feature
