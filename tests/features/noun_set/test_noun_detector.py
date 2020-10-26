import asyncio
import unittest
from src.features.noun_set import detect_nouns


class TestNounDetector(unittest.IsolatedAsyncioTestCase):
    async def assertNounText_(self, value, expected_texts):
        result = await detect_nouns(value)
        count = 0
        for expected_text in expected_texts:
            noun = result[count]
            result_text = noun.phrase
            self.assertEqual(result_text, expected_text)
            count += 1

    def test_is_defined(self):
        self.assertTrue(detect_nouns)

    async def test_returns_a_list_of_serializable_objects(self):
        result = await detect_nouns("I ran to the beach.")
        self.assertIsInstance(result, list)
        [self.assertIsInstance(noun, dict) for noun in result]

    async def test_true_positive(self):
        value = "The pretty, little girl played with her extravagant dollhouse that her mother bought the day before."
        expected = ["The pretty, little girl", "her extravagant dollhouse", "her mother", "the day"]
        await asyncio.gather(
            self.assertNounText_("I ran to you.", ["I", "you"]),
            self.assertNounText_("You ran to her.", ["You", "her"]),
            self.assertNounText_("She ran to him.", ["She", "him"]),
            self.assertNounText_("He ran to me.", ["He", "me"]),
            self.assertNounText_(value, expected),
        )

    async def test_true_negative(self):
        with self.assertRaises(TypeError):
            await detect_nouns(100)
            await detect_nouns(True)
            await detect_nouns(["I ran to the beach."])
            await detect_nouns(None)

        with self.assertRaises(ValueError):
            await detect_nouns("")
