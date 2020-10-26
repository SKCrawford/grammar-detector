import asyncio
import unittest
from src.features.verb_set import detect_verb_tense_aspect


class TestVerbTenseAspectDetector(unittest.IsolatedAsyncioTestCase):
    async def assertTenseAspect_(self, value, expected_tense, expected_aspect):
        (tense, aspect) = await detect_verb_tense_aspect(value)
        self.assertEqual(tense, expected_tense)
        self.assertEqual(aspect, expected_aspect)

    def test_is_defined(self):
        self.assertTrue(detect_verb_tense_aspect)

    async def test_returns_a_tuple_of_strings(self):
        (tense, aspect) = await detect_verb_tense_aspect("I am a test.")
        self.assertIsInstance(tense, str)
        self.assertIsInstance(aspect, str)

    async def test_true_positive(self):
        await asyncio.gather(
            self.assertTenseAspect_("I run.", "present", "simple"),
            self.assertTenseAspect_("I ran.", "past", "simple"),
            self.assertTenseAspect_("I will run.", "future", "simple"),
            self.assertTenseAspect_("I am going to run.", "future", "simple"),

            self.assertTenseAspect_("I have run.", "present", "perfect"),
            self.assertTenseAspect_("I had run.", "past", "perfect"),
            self.assertTenseAspect_("I will have run.", "future", "perfect"),

            self.assertTenseAspect_("I am running.", "present", "continuous"),
            self.assertTenseAspect_("I was running.", "past", "continuous"),
            self.assertTenseAspect_("I will be running.", "future", "continuous"),

            self.assertTenseAspect_("I have been running.", "present", "perfect continuous"),
            self.assertTenseAspect_("I had been running.", "past", "perfect continuous"),
            self.assertTenseAspect_("I will have been running.", "future", "perfect continuous"),
        )

    async def test_true_negative(self):
        with self.assertRaises(TypeError):
            await detect_verb_tense_aspect(100),
            await detect_verb_tense_aspect(True)
            await detect_verb_tense_aspect(["test string"])
            await detect_verb_tense_aspect(None)

        with self.assertRaises(ValueError):
            await detect_verb_tense_aspect("")
