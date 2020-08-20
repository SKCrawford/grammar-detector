import unittest
from enum import Enum
from src.util.validator import is_in_enum, is_truthy, is_type


class TestEnum(Enum):
    EXISTS = "exists"


class TestIsInEnumValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_in_enum)

    def test_true_positive(self):
        try:
            is_in_enum("exists", TestEnum)
        except Exception:
            self.fail("threw")

    def test_true_negative(self):
        try:
            is_in_enum("does_not_exist", TestEnum)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_false_positive(self):
        try:
            is_in_enum("EXISTS", TestEnum)
            self.fail("didn't throw")
        except Exception:
            pass


class TestIsTruthyValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_truthy)

    def test_true_positive(self):
        try:
            is_truthy("exists")
        except Exception:
            self.fail("threw")

    def test_true_negative_int(self):
        try:
            is_truthy(0)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_string(self):
        try:
            is_truthy("")
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_bool(self):
        try:
            is_truthy(False)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_list(self):
        try:
            is_truthy([])
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_None(self):
        try:
            is_truthy(None)
            self.fail("didn't throw")
        except Exception:
            pass


class TestType:
    pass


class TestIsTypeValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_type)

    def test_true_positive_string(self):
        try:
            is_type("some string", str)
        except Exception:
            self.fail("threw")

    def test_true_positive_class(self):
        try:
            is_type(TestType(), TestType)
        except Exception:
            self.fail("threw")

    def test_true_negative_string(self):
        try:
            is_type(0, str)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_class(self):
        try:
            is_type(True, TestType)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_false_positive_string(self):
        try:
            is_type(str, str)
            self.fail("didn't throw")
        except Exception:
            pass


    def test_false_positive_class(self):
        try:
            is_type(TestType, TestType)
            self.fail("didn't throw")
        except Exception:
            pass
