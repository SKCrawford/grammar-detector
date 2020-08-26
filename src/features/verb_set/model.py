class VerbFeatureSet:
    def __init__(self):
        # always a verb
        self.verb = "" 

        # past, present, future
        self.tense = "" 

        # simple, perfect, continuous, perfect continuous
        self.aspect = "" 

        # active, passive
        self.voice = "" 

        # single string phrase
        # e.g. "have be eat"
        self.lemmas = ""
