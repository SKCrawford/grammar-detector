import unittest
from enum import Enum
from src.util import validator


class TestEnum(Enum):
    EXISTS = "exists"


class TestIsInEnumValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(validator.is_in_enum)

    def test_true_positive(self):
        validator.is_in_enum("exists", TestEnum)

    def test_true_negative(self):
        self.assertRaises(ValueError, validator.is_in_enum, "does not exist", TestEnum)

    def test_false_positive(self):
        self.assertRaises(ValueError, validator.is_in_enum, "EXISTS", TestEnum)
        self.assertRaises(ValueError, validator.is_in_enum, "Exists", TestEnum)


class TestIsTruthyValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(validator.is_truthy)

    def test_true_positive(self):
        validator.is_truthy("something")
        validator.is_truthy(100)
        validator.is_truthy(True)
        validator.is_truthy(["something"])

    def test_true_negative(self):
        self.assertRaises(ValueError, validator.is_truthy, "")
        self.assertRaises(ValueError, validator.is_truthy, 0)
        self.assertRaises(ValueError, validator.is_truthy, False)
        self.assertRaises(ValueError, validator.is_truthy, [])
        self.assertRaises(ValueError, validator.is_truthy, None)


class TestType:
    pass


class TestIsTypeValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(validator.is_type)

    def test_true_positive(self):
        validator.is_type("some string", str)
        validator.is_type("", str)
        validator.is_type(TestType(), TestType)

    def test_true_negative(self):
        self.assertRaises(TypeError, validator.is_type, 0, str)
        self.assertRaises(TypeError, validator.is_type, True, str)
        self.assertRaises(TypeError, validator.is_type, [], str)
        self.assertRaises(TypeError, validator.is_type, None, str)
        self.assertRaises(TypeError, validator.is_type, TestType, str)
        self.assertRaises(TypeError, validator.is_type, "", TestType)
        self.assertRaises(TypeError, validator.is_type, 0, TestType)
        self.assertRaises(TypeError, validator.is_type, True, TestType)
        self.assertRaises(TypeError, validator.is_type, [], TestType)
        self.assertRaises(TypeError, validator.is_type, None, TestType)

    def test_false_positive(self):
        self.assertRaises(TypeError, validator.is_type, str, str)
        self.assertRaises(TypeError, validator.is_type, TestType, TestType)


class TestIsNotTypeValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(validator.is_not_type)

    def test_true_positive(self):
        validator.is_not_type("some string", int)
        validator.is_not_type("some string", bool)
        validator.is_not_type("some string", list)
        validator.is_not_type("some string", type(None))
        validator.is_not_type("some string", TestType)

        validator.is_not_type(100, str)
        validator.is_not_type(100, bool)
        validator.is_not_type(100, list)
        validator.is_not_type(100, type(None))
        validator.is_not_type(100, TestType)

        validator.is_not_type(True, str)
        validator.is_not_type(True, list)
        validator.is_not_type(True, type(None))
        validator.is_not_type(True, TestType)

        validator.is_not_type([], str)
        validator.is_not_type([], int)
        validator.is_not_type([], bool)
        validator.is_not_type([], type(None))
        validator.is_not_type([], TestType)

        validator.is_not_type(None, str)
        validator.is_not_type(None, int)
        validator.is_not_type(None, bool)
        validator.is_not_type(None, list)
        validator.is_not_type(None, TestType)

        validator.is_not_type(TestType, str)
        validator.is_not_type(TestType, int)
        validator.is_not_type(TestType, bool)
        validator.is_not_type(TestType, list)
        validator.is_not_type(TestType, type(None))

    def test_true_negative(self):
        self.assertRaises(TypeError, validator.is_not_type, "some string", str)
        self.assertRaises(TypeError, validator.is_not_type, "", str)
        self.assertRaises(TypeError, validator.is_not_type, 100, int)
        self.assertRaises(TypeError, validator.is_not_type, 0, int)
        self.assertRaises(TypeError, validator.is_not_type, True, bool)
        self.assertRaises(TypeError, validator.is_not_type, False, bool)
        self.assertRaises(TypeError, validator.is_not_type, True, int)
        self.assertRaises(TypeError, validator.is_not_type, False, int)
        self.assertRaises(TypeError, validator.is_not_type, ["some string"], list)
        self.assertRaises(TypeError, validator.is_not_type, [], list)
        self.assertRaises(TypeError, validator.is_not_type, TestType(), TestType)
        self.assertRaises(TypeError, validator.is_not_type, None, type(None))
