class VerbFeatureSet:
    def __init__(self):
        # always VerbFeatures
        self.verbs = []

        # past, present, future
        self.tense = "" 

        # simple, perfect, continuous, perfect continuous
        self.aspect = "" 

        # active, passive
        self.voice = None
