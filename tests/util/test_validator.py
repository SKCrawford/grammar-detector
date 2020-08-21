from enum import Enum


class TestEnum(Enum):
    EXISTS = "exists"


class TestIsInEnumValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_in_enum)

    def test_true_positive(self):
        is_in_enum("exists", TestEnum)

    def test_true_negative(self):
        self.assertRaises(ValueError, is_in_enum, "does not exist", TestEnum)

    def test_false_positive(self):
        self.assertRaises(ValueError, is_in_enum, "EXISTS", TestEnum)
        self.assertRaises(ValueError, is_in_enum, "Exists", TestEnum)


class TestIsTruthyValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_truthy)

    def test_true_positive(self):
        is_truthy("something")
        is_truthy(100)
        is_truthy(True)
        is_truthy(["something"])

    def test_true_negative(self):
        self.assertRaises(ValueError, is_truthy, "")
        self.assertRaises(ValueError, is_truthy, 0)
        self.assertRaises(ValueError, is_truthy, False)
        self.assertRaises(ValueError, is_truthy, [])
        self.assertRaises(ValueError, is_truthy, None)


class TestType:
    pass


class TestIsTypeValidator(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(is_type)

    def test_true_positive(self):
        is_type("some string", str)
        is_type("", str)
        is_type(TestType(), TestType)

    def test_true_negative(self):
        self.assertRaises(TypeError, is_type, 0, str)
        self.assertRaises(TypeError, is_type, True, str)
        self.assertRaises(TypeError, is_type, [], str)
        self.assertRaises(TypeError, is_type, None, str)
        self.assertRaises(TypeError, is_type, TestType, str)
        self.assertRaises(TypeError, is_type, "", TestType)
        self.assertRaises(TypeError, is_type, 0, TestType)
        self.assertRaises(TypeError, is_type, True, TestType)
        self.assertRaises(TypeError, is_type, [], TestType)
        self.assertRaises(TypeError, is_type, None, TestType)

    def test_false_positive(self):
        self.assertRaises(TypeError, is_type, str, str)
        self.assertRaises(TypeError, is_type, TestType, TestType)
