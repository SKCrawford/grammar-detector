import unittest
from src.core.pattern import validator


class TestPatternValidator(unittest.TestCase):
    def test_pattern_validator_is_defined(self):
        self.assertTrue(validator.validate_pattern)

    def test_name_validator_is_defined(self):
        self.assertTrue(validator._validate_name)

    def test_tokens_validator_is_defined(self):
        self.assertTrue(validator._validate_tokens)

    def test_pattern_validator_true_positive(self):
        name = "test pattern"
        tokens = [{ "POS": "NOUN" }, { "POS": "VERB", "DEP": "ROOT" }]
        result = validator.validate_pattern(name, tokens)
        self.assertTrue(result)

    def test_pattern_validator_true_negative(self):
        name = 100
        tokens = [{ "POS": "NOUN" }, { "POS": "VERB", "DEP": "ROOT" }]
        self.assertRaises(TypeError, validator.validate_pattern, name, tokens)
        name = "test pattern"
        tokens = 100
        self.assertRaises(TypeError, validator.validate_pattern, name, tokens)


class TestPatternValidator(unittest.TestCase):
    def test_name_validator_is_defined(self):
        self.assertTrue(validator._validate_name)

    def test_name_validator_true_positive(self):
        name = "test pattern"
        validator._validate_name(name)

    def test_name_validator_true_negative(self):
        name = 100
        self.assertRaises(TypeError, validator._validate_name, name)
        name = []
        self.assertRaises(TypeError, validator._validate_name, name)
        name = ""
        self.assertRaises(ValueError, validator._validate_name, name)



class TestTokensValidator(unittest.TestCase):
    def test_tokens_validator_is_defined(self):
        self.assertTrue(validator._validate_tokens)

    def test_tokens_validator_true_positive(self):
        tokens = [{ "POS": "NOUN" }, { "POS": "VERB", "DEP": "ROOT" }]
        validator._validate_tokens(tokens)

    def test_tokens_validator_true_negative(self):
        tokens = 100
        self.assertRaises(TypeError, validator._validate_tokens, tokens)
        tokens = ""
        self.assertRaises(TypeError, validator._validate_tokens, tokens)
        tokens = []
        self.assertRaises(ValueError, validator._validate_tokens, tokens)
