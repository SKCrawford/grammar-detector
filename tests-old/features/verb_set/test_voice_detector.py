import unittest
from src.features.verb_set import detect_verb_voice


class TestVerbVoiceDetector(unittest.IsolatedAsyncioTestCase):
    async def assertVoice_(self, sentence, expected_voice):
        result = await detect_verb_voice(sentence)
        self.assertEqual(result, expected_voice)

    def test_is_defined(self):
        self.assertTrue(detect_verb_voice)

    async def test_returns_a_string(self):
        voice = await detect_verb_voice("The cat was chased by the dog.")
        self.assertIsInstance(voice, str)

    async def test_true_positive(self):
        await self.assertVoice_("The cat was chased by the dog.", "passive")

    async def test_true_negative(self):
        with self.assertRaises(TypeError):
            await detect_verb_voice(100)
            await detect_verb_voice(True)
            await detect_verb_voice(["test string"])
            await detect_verb_voice(None)

        with self.assertRaises(ValueError):
            await detect_verb_voice("")
