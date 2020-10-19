from src.core.feature.model import PhraseFeature


class NounFeature(PhraseFeature):
    def __init__(self):
        super()

        # a PersonFeature
        self.person = None
