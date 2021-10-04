import unittest
from enum import Enum
from src.util.decorator import is_in_enum, is_truthy, is_type


class TestEnum(Enum):
    EXISTS = "exists"


@is_in_enum(TestEnum)
def is_in_enum_func(value):
        pass


class TestIsInEnumDecorator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_in_enum)
        self.assertTrue(is_in_enum_func)

    def test_true_positive(self):
        is_in_enum_func("exists")

    def test_true_negative(self):
        self.assertRaises(ValueError, is_in_enum_func, "does not exist")

    def test_false_positive(self):
        self.assertRaises(ValueError, is_in_enum_func, "EXISTS")
        self.assertRaises(ValueError, is_in_enum_func, "Exists")


@is_truthy
def is_truthy_func(value):
    pass


class TestIsTruthyDecorator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_truthy)
        self.assertTrue(is_truthy_func)

    def test_true_positive(self):
        is_truthy_func("something")
        is_truthy_func(100)
        is_truthy_func(True)
        is_truthy_func(["something"])

    def test_true_negative(self):
        self.assertRaises(ValueError, is_truthy_func, "")
        self.assertRaises(ValueError, is_truthy_func, 0)
        self.assertRaises(ValueError, is_truthy_func, False)
        self.assertRaises(ValueError, is_truthy_func, [])
        self.assertRaises(ValueError, is_truthy_func, None)


class TestType:
    pass


@is_type(str)
def is_type_string_func(value):
    pass


@is_type(TestType)
def is_type_class_func(value):
    pass


class TestIsTypeDecorator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_type)
        self.assertTrue(is_type_string_func)
        self.assertTrue(is_type_class_func)

    def test_true_positive(self):
        is_type_string_func("some string")
        is_type_string_func("")
        is_type_class_func(TestType())

    def test_true_negative(self):
        self.assertRaises(TypeError, is_type_string_func, 0)
        self.assertRaises(TypeError, is_type_string_func, True)
        self.assertRaises(TypeError, is_type_string_func, [])
        self.assertRaises(TypeError, is_type_string_func, None)
        self.assertRaises(TypeError, is_type_string_func, TestType)
        self.assertRaises(TypeError, is_type_class_func, "")
        self.assertRaises(TypeError, is_type_class_func, 0)
        self.assertRaises(TypeError, is_type_class_func, True)
        self.assertRaises(TypeError, is_type_class_func, [])
        self.assertRaises(TypeError, is_type_class_func, None)

    def test_false_positive(self):
        self.assertRaises(TypeError, is_type_string_func, str)
        self.assertRaises(TypeError, is_type_class_func, TestType)
