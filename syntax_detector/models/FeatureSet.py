from ..enums import *


class FeatureSet:
    raw_sentence = ""

    # noun type
    subject = ""

    verb = ""

    # noun type
    object = ""

    # past, present, future
    tense = ""

    # simple, perfect, continuous, perfect continuous
    aspect = ""

    # if True, verb is VBZ; if False, verb is VBP
    is_third_person = False

    # active, passive
    voice = ""

    # declarative, interrogative, exclamatory, imperative
    purpose = "" 

    # names/proper nouns
    names = []

    # the terminating punctuation of the sentence
    ending_punct = ""


    def __init__(self, sentence):
        if not isinstance(sentence, str):
            raise TypeError("expected a string")
        if not sentence:
            raise ValueError("expected a truthy string")

        self.raw_sentence = sentence
        self._load()

    def _load(self):
        # TODO
        pass
