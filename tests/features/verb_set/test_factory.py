import unittest
from src.features.verb_set.factory import VerbFeatureSetFactory
from src.features.verb_set.model import VerbFeatureSet


class TestVerbFeatureSetFactory(unittest.TestCase):
    factory = None

    def setUp(self):
        self.factory = VerbFeatureSetFactory()

    def test_is_defined(self):
        self.assertTrue(VerbFeatureSetFactory)

    def test_is_constructable(self):
        self.assertTrue(VerbFeatureSetFactory())

    def test_can_spawn_product_instance(self):
        self.assertIsInstance(VerbFeatureSetFactory, self.factory)
        self.assertTrue(self.factory)

    def test_has_no_product_instance_until_spawn(self):
        self.assertFalse(self.factory._instance)
        self.factory._spawn()
        self.assertTrue(self.factory._instance)

    def test_can_build_complete_product_instance(self):
        instance = self.factory.build()
        self.assertIsInstance(instance, VerbFeatureSet)
        self.assertTrue(instance)
        self.assertIsInstance(instance.verb, str)
        self.assertIsInstance(instance.tense, str)
        self.assertIsInstance(instance.aspect, str)
        self.assertTrue(instance.verb)
        self.assertTrue(instance.tense)
        self.assertTrue(instance.aspect)
