import unittest
from src.features.noun_set.builder import NounFeatureSetBuilder
from src.features.noun_set.model import NounFeatureSet
from src.features.noun_set.noun.model import Noun


class TestNounFeatureSetBuilder(unittest.TestCase):
    builder = None

    def setUp(self):
        self.builder = NounFeatureSetBuilder()

    def test_is_defined(self):
        self.assertTrue(NounFeatureSetBuilder)

    def test_is_constructable(self):
        self.assertTrue(NounFeatureSetBuilder())

    def test_can_spawn_product_instance(self):
        self.assertIsInstance(self.builder, NounFeatureSetBuilder)
        self.assertTrue(self.builder)

    def test_has_no_product_instance_until_spawn(self):
        self.assertFalse(self.builder._instance)
        self.builder.spawn()
        self.assertTrue(self.builder._instance)

    def test_can_build_complete_product_instance(self):
        instance = NounFeatureSetBuilder()  \
            .spawn()                        \
            .set_attr('nouns', [Noun()])    \
            .set_attr('person', "1st")      \
            .build()
        self.assertIsInstance(instance, NounFeatureSet)
        self.assertTrue(instance)
        self.assertIsInstance(instance.nouns, list)
        [self.assertIsInstance(noun, Noun) for noun in instance.nouns]
        self.assertIsInstance(instance.person, str)
        self.assertTrue(instance.person)
