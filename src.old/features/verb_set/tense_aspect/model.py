from src.core.feature.model import SimpleFeature


class TenseAspectFeature(SimpleFeature):
    def __init__(self):
        super()
        self.name = "tense aspect"
        self.value = {
            "tense": "",
            "aspect": "",
        }
