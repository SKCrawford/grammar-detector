import unittest
from src.util.builder import Builder
from src.features.verb_set.model import VerbFeatureSet


class TestBuilder(unittest.TestCase):
    builder = None

    def setUp(self):
        self.builder = Builder(VerbFeatureSet)

    def test_is_defined(self):
        self.assertTrue(Builder)

    def test_is_constructable(self):
        self.assertTrue(Builder(VerbFeatureSet))

    def test_can_spawn_product_instance(self):
        self.assertIsInstance(self.builder, Builder)
        self.assertTrue(self.builder)

    def test_has_no_product_instance_until_spawned(self):
        self.assertFalse(self.builder._instance)
        self.builder.spawn()
        self.assertTrue(self.builder._instance)

    def test_can_build_complete_product_instance(self):
        instance = Builder(VerbFeatureSet)              \
            .set_attr('verb', "have been running")      \
            .set_attr('tense', "present")               \
            .set_attr('aspect', "perfect continuous")   \
            .build()
        self.assertIsInstance(instance, VerbFeatureSet)
        self.assertTrue(instance)
        self.assertIsInstance(instance.verb, str)
        self.assertIsInstance(instance.tense, str)
        self.assertIsInstance(instance.aspect, str)
        self.assertTrue(instance.verb)
        self.assertTrue(instance.tense)
        self.assertTrue(instance.aspect)
