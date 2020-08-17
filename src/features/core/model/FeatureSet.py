_default_string = "???"
_default_ending_punct = "->???<-"


class FeatureSet:
    """A dictionary of the linguistic features of a sentence. The sentence
    itself is also exposed. This is intended to be used in conjunction
    with the Builder to create and set instances. It is not intended to
    call the constructor manually.
    """

    # the untokenized sentence
    sentence = _default_string

    # always a noun
    subject = _default_string

    # always a verb
    verb = _default_string

    # always a noun
    object = _default_string

    # past, present, future
    tense = _default_string

    # simple, perfect, continuous, perfect continuous
    aspect = _default_string

    # first, second, third
    person = _default_string

    # active, passive
    voice = _default_string

    # declarative, interrogative, exclamatory, imperative
    purpose = _default_string 

    # names/proper nouns
    names = []

    # the terminating punctuation of the sentence
    ending_punct = _default_ending_punct
