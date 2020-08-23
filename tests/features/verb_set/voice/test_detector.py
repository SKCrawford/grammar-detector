import unittest
from src.features.verb_set.voice.detector import detect_verb_voice


class TestVerbVoiceDetector(unittest.TestCase):
    def assertVoice_(self, value, expected_voice):
        result = detect_verb_voice(value)
        self.assertEqual(result, expected_voice)

    def test_is_defined(self):
        self.assertTrue(detect_verb_voice)

    def test_returns_a_string(self):
        voice = detect_verb_voice("The cat was chased by the dog.")
        self.assertIsInstance(voice, str)

    def test_true_positive(self):
        self.assertVoice_("The cat was chased by the dog.", "passive")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_voice, 100)
        self.assertRaises(TypeError, detect_verb_voice, True)
        self.assertRaises(TypeError, detect_verb_voice, ["test string"])
        self.assertRaises(TypeError, detect_verb_voice, None)

    def test_false_positive(self):
        self.assertRaises(ValueError, detect_verb_voice, "")
