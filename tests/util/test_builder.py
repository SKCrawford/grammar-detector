import unittest
from src.util.builder import Builder


class Foo:
    def __init__(self):
        self.bar = ""
        self.baz = ""


class TestBuilder(unittest.TestCase):
    builder = None

    def setUp(self):
        self.builder = Builder(Foo)

    def test_is_defined(self):
        self.assertTrue(Builder)

    def test_is_constructable(self):
        self.assertTrue(Builder(Foo))

    def test_can_spawn_product_instance(self):
        self.assertIsInstance(self.builder, Builder)
        self.assertTrue(self.builder)

    def test_has_no_product_instance_until_spawned(self):
        self.assertFalse(self.builder._instance)
        self.builder.spawn()
        self.assertTrue(self.builder._instance)

    def test_can_build_complete_product_instance(self):
        instance = Builder(Foo)         \
            .set_attr("bar", "foobar")  \
            .set_attr("baz", "foobaz")  \
            .build()
        self.assertIsInstance(instance, Foo)
        self.assertTrue(instance)
        self.assertIsInstance(instance.bar, str)
        self.assertIsInstance(instance.baz, str)
        self.assertTrue(instance.bar)
        self.assertTrue(instance.baz)
