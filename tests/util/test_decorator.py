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

    def test_true_positive(self):
        try:
            is_in_enum_func("exists")
        except Exception:
            self.fail("threw")

    def test_true_negative(self):
        try:
            is_in_enum_func("does_not_exist")
            self.fail("didn't throw")
        except Exception:
            pass

    def test_false_positive(self):
        try:
            is_in_enum_func("EXISTS")
            self.fail("didn't throw")
        except Exception:
            pass


@is_truthy
def is_truthy_func(value):
    pass


class TestIsTruthyDecorator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_truthy)

    def test_true_positive(self):
        try:
            is_truthy_func("exists")
        except Exception:
            self.fail("threw")

    def test_true_negative_int(self):
        try:
            is_truthy_func(0)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_string(self):
        try:
            is_truthy_func("")
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_bool(self):
        try:
            is_truthy_func(False)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_list(self):
        try:
            is_truthy_func([])
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_None(self):
        try:
            is_truthy_func(None)
            self.fail("didn't throw")
        except Exception:
            pass


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

    def test_true_positive_string(self):
        try:
            is_type_string_func("some string")
        except Exception:
            self.fail("threw")

    def test_true_positive_class(self):
        try:
            is_type_class_func(TestType())
        except Exception:
            self.fail("threw")

    def test_true_negative_string(self):
        try:
            is_type_string_func(0)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_true_negative_class(self):
        try:
            is_type_class_func(True)
            self.fail("didn't throw")
        except Exception:
            pass

    def test_false_positive_string(self):
        try:
            is_type_string_func(str)
            self.fail("didn't throw")
        except Exception:
            pass


    def test_false_positive_class(self):
        try:
            is_type_class_func(TestType)
            self.fail("didn't throw")
        except Exception:
            pass
