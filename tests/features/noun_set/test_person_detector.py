import unittest
from src.features.noun_set import detect_noun_person


class TestNounPersonDetector(unittest.TestCase):
    async def assertPerson_(self, value, expected_person):
        result = await detect_noun_person(value)
        self.assertEqual(result, expected_person)

    def test_is_defined(self):
        self.assertTrue(detect_noun_person)

    async def test_returns_a_string(self):
        person = await detect_noun_person("She is running for President.")
        self.assertIsInstance(person, str)

    async def test_true_positive(self):
        await asyncio.gather(
            self.assertPerson_("I am running for President.", "1st"),
            self.assertPerson_("We are running for President.", "1st"),
            self.assertPerson_("You are running for President.", "2nd"),
            self.assertPerson_("She is running for President.", "3rd"),
            self.assertPerson_("They are running for President.", "3rd"),
            self.assertPerson_("Amy is running for President.", "3rd"),
            self.assertPerson_("Biden and Harris are running for President.", "3rd"),
        )

    async def test_true_negative(self):
        with self.assertRaises(TypeError):
            await detect_noun_person(100)
            await detect_noun_person(True)
            await detect_noun_person(["She is running for President."])
            await detect_noun_person(None)

        with self.assertRaises(ValueError):
            await detect_noun_person("")
