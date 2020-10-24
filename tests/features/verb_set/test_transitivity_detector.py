import unittest
from src.features.verb_set import detect_verb_transitivity


class TestVerbTransitivityDetector(unittest.TestCase):
    def assertTransitivity_(self, input, expected_transitivity, expected_valency):
        (result_transitivity, result_valency) = detect_verb_transitivity(input)
        self.assertEqual(result_transitivity, expected_transitivity)
        self.assertEqual(result_valency, expected_valency)

    def test_is_defined(self):
        self.assertTrue(detect_verb_transitivity)

    def test_returns_a_tuple_of_str_and_int(self):
        match = detect_verb_transitivity("The dog chased the cat.")
        self.assertIsInstance(match, tuple)

        (transitivity, valency) = match
        self.assertIsInstance(transitivity, str)
        self.assertIsInstance(valency, int)

    def test_true_positive_impersonal(self):
        # simple
        self.assertTransitivity_("It rains.", "impersonal", 0)
        self.assertTransitivity_("It rained.", "impersonal", 0)
        self.assertTransitivity_("It will rain.", "impersonal", 0)

        # continuous
        self.assertTransitivity_("It is raining.", "impersonal", 0)
        self.assertTransitivity_("It was raining.", "impersonal", 0)
        self.assertTransitivity_("It will be raining.", "impersonal", 0)

        # perfect
        self.assertTransitivity_("It has rained.", "impersonal", 0)
        self.assertTransitivity_("It had rained.", "impersonal", 0)
        self.assertTransitivity_("It will have rained.", "impersonal", 0)

        # perfect continuous
        self.assertTransitivity_("It has been raining.", "impersonal", 0)
        self.assertTransitivity_("It had been raining.", "impersonal", 0)
        self.assertTransitivity_("It will have been raining.", "impersonal", 0)

    def test_true_positive_intransitive(self):
        # simple
        self.assertTransitivity_("She runs.", "intransitive", 1)
        self.assertTransitivity_("She ran.", "intransitive", 1)
        self.assertTransitivity_("She will run.", "intransitive", 1)

        # continuous
        self.assertTransitivity_("She is running.", "intransitive", 1)
        self.assertTransitivity_("She was running.", "intransitive", 1)
        self.assertTransitivity_("She will be running.", "intransitive", 1)

        # perfect
        self.assertTransitivity_("She has run.", "intransitive", 1)
        self.assertTransitivity_("She had run", "intransitive", 1)
        self.assertTransitivity_("She will have run.", "intransitive", 1)

        # perfect continuous
        self.assertTransitivity_("She has been running.", "intransitive", 1)
        self.assertTransitivity_("She had been running.", "intransitive", 1)
        self.assertTransitivity_("She will have been running.", "intransitive", 1)

    def test_true_positive_transitive(self):
        # simple
        self.assertTransitivity_("She plays tennis.", "transitive", 2)
        self.assertTransitivity_("She played tennis.", "transitive", 2)
        self.assertTransitivity_("She will play tennis.", "transitive", 2)

        # continuous
        self.assertTransitivity_("She is playing tennis.", "transitive", 2)
        self.assertTransitivity_("She was playing tennis.", "transitive", 2)
        self.assertTransitivity_("She will be playing tennis.", "transitive", 2)

        # perfect
        self.assertTransitivity_("She has played tennis.", "transitive", 2)
        self.assertTransitivity_("She had played tennis.", "transitive", 2)
        self.assertTransitivity_("She will have played tennis.", "transitive", 2)

        # perfect continuous
        self.assertTransitivity_("She has been playing tennis.", "transitive", 2)
        self.assertTransitivity_("She had been playing tennis.", "transitive", 2)
        self.assertTransitivity_("She will have been playing tennis.", "transitive", 2)

    def test_true_positive_ditransitive_dobj_prep_pobj(self):
        # simple
        self.assertTransitivity_("He gives the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He gave the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He will give the rose to her.", "ditransitive", 3)

        # continuous
        self.assertTransitivity_("He is giving the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He was giving the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He will be giving the rose to her.", "ditransitive", 3)

        # perfect
        self.assertTransitivity_("He has given the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He had given the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He will have given the rose to her.", "ditransitive", 3)

        # perfect continuous
        self.assertTransitivity_("He has been giving the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He had been giving the rose to her.", "ditransitive", 3)
        self.assertTransitivity_("He will have been giving the rose to her.", "ditransitive", 3)

    def test_true_positive_ditransitive_dative_det_dobj(self):
        # simple
        self.assertTransitivity_("He gives her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He gave her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He will give her the rose.", "ditransitive", 3)

        # continuous
        self.assertTransitivity_("He is giving her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He was giving her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He will be giving her the rose.", "ditransitive", 3)

        # perfect
        self.assertTransitivity_("He has given her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He had given her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He will have given her the rose.", "ditransitive", 3)

        # perfect continuous
        self.assertTransitivity_("He has been giving her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He had been giving her the rose.", "ditransitive", 3)
        self.assertTransitivity_("He will have been giving her the rose.", "ditransitive", 3)

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_transitivity, 100)
        self.assertRaises(TypeError, detect_verb_transitivity, True)
        self.assertRaises(TypeError, detect_verb_transitivity, ["It rained."])
        self.assertRaises(TypeError, detect_verb_transitivity, None)
        self.assertRaises(ValueError, detect_verb_transitivity, "")
