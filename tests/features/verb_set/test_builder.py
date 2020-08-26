import unittest
from src.features.verb_set.builder import VerbFeatureSetBuilder
from src.features.verb_set.model import VerbFeatureSet


class TestVerbFeatureSetBuilder(unittest.TestCase):
    builder = None

    def setUp(self):
        self.builder = VerbFeatureSetBuilder()

    def test_is_defined(self):
        self.assertTrue(VerbFeatureSetBuilder)

    def test_is_constructable(self):
        self.assertTrue(VerbFeatureSetBuilder())

    def test_can_spawn_product_instance(self):
        self.assertIsInstance(self.builder, VerbFeatureSetBuilder)
        self.assertTrue(self.builder)

    def test_has_no_product_instance_until_spawn(self):
        self.assertFalse(self.builder._instance)
        self.builder.spawn()
        self.assertTrue(self.builder._instance)

    def test_can_build_complete_product_instance(self):
        instance = VerbFeatureSetBuilder()              \
            .spawn()                                    \
            .set_attr('verb', "have been running")      \
            .set_attr('tense', "present")               \
            .set_attr('aspect', "perfect continuous")   \
            .set_attr('voice', "active")                \
            .set_attr('person', "1st")                  \
            .set_attr('lemmas', "have be run")          \
            .build()
        self.assertIsInstance(instance, VerbFeatureSet)
        self.assertTrue(instance)
        self.assertIsInstance(instance.verb, str)
        self.assertIsInstance(instance.tense, str)
        self.assertIsInstance(instance.aspect, str)
        self.assertTrue(instance.verb)
        self.assertTrue(instance.tense)
        self.assertTrue(instance.aspect)
