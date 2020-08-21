import unittest
from src.features.sentence_set.builder import SentenceFeatureSetBuilder
from src.features.sentence_set.model import SentenceFeatureSet
from src.features.verb_set.model import VerbFeatureSet


class TestSentenceFeatureSetBuilder(unittest.TestCase):
    builder = None

    def setUp(self):
        self.builder = SentenceFeatureSetBuilder()

    def test_is_defined(self):
        self.assertTrue(SentenceFeatureSetBuilder)

    def test_is_constructable(self):
        self.assertTrue(SentenceFeatureSetBuilder())

    def test_can_spawn_instance(self):
        self.assertIsNone(self.builder._instance)
        self.builder.spawn()
        self.assertIsInstance(self.builder._instance, SentenceFeatureSet)
        self.assertTrue(self.builder._instance)

    def test_can_build_instance(self):
        self.builder.spawn()
        instance = self.builder.build()
        self.assertIsInstance(instance, SentenceFeatureSet)
        self.assertTrue(instance)

    def test_can_set_sentence(self):
        self.builder.spawn()
        self.assertIsInstance(self.builder._instance.sentence, str)
        self.assertFalse(self.builder._instance.sentence)
        self.builder.set_sentence("I am a test.")
        self.assertIsInstance(self.builder._instance.sentence, str)
        self.assertTrue(self.builder._instance.sentence)

    def test_can_set_verb_feature_set(self):
        self.builder.spawn()
        self.assertFalse(self.builder._instance.verb_features)
        verb_f_set = VerbFeatureSet()
        self.builder.set_verb_feature_set(verb_f_set)
        self.assertIsInstance(self.builder._instance.verb_features, VerbFeatureSet)
        self.assertTrue(self.builder._instance.verb_features)
