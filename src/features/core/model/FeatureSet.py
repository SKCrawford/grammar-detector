class FeatureSet:
    # the untokenized sentence
    sentence = ""

    # always a noun
    subject = ""

    # always a verb
    verb = ""

    # always a noun
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
