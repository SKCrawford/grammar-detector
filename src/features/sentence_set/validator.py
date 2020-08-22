from src.util.decorator import is_truthy, is_type
from ..verb_set.model import VerbFeatureSet
from .model import SentenceFeatureSet


def validate_sentence_feature_set(feature_set):
    """Validate a SentenceFeatureSet instance.

    Given a SentenceFeatureSet instance, return void.
    """
    _validate_feature_set(feature_set)
    _validate_sentence(feature_set.sentence)


@is_type(SentenceFeatureSet)
@is_truthy
def _validate_feature_set(feature_set):
    pass


@is_type(str)
@is_truthy
def _validate_sentence(sentence):
    pass
