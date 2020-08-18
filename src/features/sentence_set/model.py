class SentenceFeatureSet:
    """A dictionary of the linguistic features of a sentence. The sentence
    itself is also exposed. This is intended to be used in conjunction
    with the SentenceFeatureSetBuilder to create and modify instances.
    It is not intended to call the constructor manually.
    """

    # the untokenized sentence
    sentence = ""

    # features relating to the verb
    verb_features = None
