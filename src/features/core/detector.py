from src.enum.Feature import Feature
from src.util.Builder import Builder
from ..verb_tense.detector import detect_verb_features
from .model.FeatureSet import FeatureSet
from .model.FeatureSetValidator import FeatureSetValidator


def detect_features(sentence):
    """Determine the linguistic features of a sentence.
    
    Given a string, return a FeatureSet instance.
    """

    verb_features = detect_verb_features(sentence)
    (tense, aspect, verb) = verb_features

    builder = Builder(FeatureSet, FeatureSetValidator)
    f_set = builder.spawn()                                     \
        .set(Feature.SENTENCE.value, sentence)                  \
        .set(Feature.VERB.value, verb)                          \
        .set(Feature.TENSE.value, tense)                        \
        .set(Feature.ASPECT.value, aspect)                      \
        .build()                                                \
        #  # TODO
        #  .set(Feature.PERSON.value, person)                   \
        #  .set(Feature.SUBJECT.value, "???")                   \
        #  .set(Feature.OBJECT.value, "???")                    \
        #  .set(Feature.VOICE.value, "???")                     \
        #  .set(Feature.PURPOSE.value, "???")                   \
        #  .set(Feature.NAMES.value, [])                        \
        #  .set(Feature.ENDING_PUNCT.value, "->???<-")          \
    return f_set
