class SimpleFeature:
    """A bridge Implementor interface for features with a name and a value.
    A good example would be verb tense/aspect, verb voice, or noun person."""

    def __init__(self):
        # the name of the feature (e.g. tense)
        self.name = ""

        # the value of the feature (e.g. present)
        self.value = None

    def __str__(self):
        return f"{self.name.title()}: {self.value}"


class PhraseFeature:
    """A bridge Implementor interface for phrasal features."""

    def __init__(self):
        # the phrase's text
        self.phrase = ""

        # the phrase root's text
        self.root = ""

        # the phrase root's head
        self.root_head = ""

        # the phrase root's part of speech
        self.pos = ""

        # the phrase root's tag
        self.tag = ""

        # the phrase root's dependency label
        self.dep = ""

        # the phrase's lemmas
        self.phrase_lemma = ""

        # the phrase root's lemma
        self.root_lemma = ""

        # the explained part of speech
        self.pos_desc = ""

        # the explained tag
        self.tag_desc = ""

        # the explained dependency label
        self.dep_desc = ""

    def __str__(self):
        return f"{self.phrase} ({self.tag}/{self.dep})"
