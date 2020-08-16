from ..enums.TenseAspect import TenseAspect
from ..models.PatternSet import PatternSet


def create_verb_tense_pattern_set():
    p_set = PatternSet("verb tenses")

    # Simple
    p_set.create(TenseAspect.PRESENT_SIMPLE.value, [
        {"TAG": "VBP", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.PRESENT_SIMPLE_3.value, [
        {"TAG": "VBZ", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.PAST_SIMPLE.value, [
        {"TAG": "VBD", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.FUTURE_SIMPLE_WILL.value, [
        {"TAG": "MD", "DEP": "aux", "OP": "+", "LOWER": "will"},
        {"TAG": "VB", "DEP": "ROOT", "OP": "+"}
    ])
    p_set.create(TenseAspect.FUTURE_SIMPLE_BE_GOING_TO.value, [
        {"TAG": "VBP", "DEP": "aux", "OP": "+"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+", "LEMMA": "go"},
        {"TAG": "TO", "DEP": "aux", "OP": "+"},
        {"TAG": "VB", "DEP": "xcomp", "OP": "+"},
    ])
    p_set.create(TenseAspect.FUTURE_SIMPLE_BE_GOING_TO_3.value, [
        {"TAG": "VBZ", "DEP": "aux", "OP": "+"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+", "LEMMA": "go"},
        {"TAG": "TO", "DEP": "aux", "OP": "+"},
        {"TAG": "VB", "DEP": "xcomp", "OP": "+"},
    ])

    # Continuous/progressive
    # TODO: fix tokens 3-4
    p_set.create(TenseAspect.PRESENT_CONT.value, [
        {"TAG": "VBP", "DEP": "aux", "OP": "+"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
        {"TAG": "TO", "DEP": "aux", "OP": "?"},
        {"TAG": "VB", "DEP": "xcomp", "OP": "!"},
    ])
    # TODO: fix tokens 3-4
    p_set.create(TenseAspect.PRESENT_CONT_3.value, [
        {"TAG": "VBZ", "DEP": "aux", "OP": "+"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
        {"TAG": "TO", "DEP": "aux", "OP": "?"},
        {"TAG": "VB", "DEP": "xcomp", "OP": "!"},
    ])
    p_set.create(TenseAspect.PAST_CONT.value, [
        {"TAG": "VBD", "DEP": "aux", "OP": "+"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.FUTURE_CONT.value, [
        {"TAG": "MD", "DEP": "aux", "OP": "+", "LEMMA": "will"},
        {"TAG": "VB", "DEP": "aux", "OP": "+", "LEMMA": "be"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
    ])

    # Perfect
    p_set.create(TenseAspect.PRESENT_PERF.value, [
        {"TAG": "VBP", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.PRESENT_PERF_3.value, [
        {"TAG": "VBZ", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "ROOT", "OP": "+"},
    ])
    # TODO: add support for passive
    p_set.create(TenseAspect.PAST_PERF.value, [
        {"TAG": "VBD", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.FUTURE_PERF.value, [
        {"TAG": "MD", "DEP": "aux", "OP": "+", "LEMMA": "will"},
        {"TAG": "VB", "DEP": "aux", "OP": "+"},
        {"TAG": "VBN", "DEP": "ROOT", "OP": "+"},
    ])

    # Perfect continuous/progressive
    p_set.create(TenseAspect.PRESENT_PERF_CONT.value, [
        {"TAG": "VBP", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "aux", "OP": "+"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.PRESENT_PERF_CONT_3.value, [
        {"TAG": "VBZ", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "aux", "OP": "+", "LEMMA": "be"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.PAST_PERF_CONT.value, [
        {"TAG": "VBD", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "aux", "OP": "+", "LEMMA": "be"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
    ])
    p_set.create(TenseAspect.FUTURE_PERF_CONT.value, [
        {"TAG": "MD", "DEP": "aux", "OP": "+", "LEMMA": "will"},
        {"TAG": "VB", "DEP": "aux", "OP": "+", "LEMMA": "have"},
        {"TAG": "VBN", "DEP": "aux", "OP": "+", "LEMMA": "be"},
        {"TAG": "VBG", "DEP": "ROOT", "OP": "+"},
    ])

    return p_set


verb_tense_pattern_set = create_verb_tense_pattern_set()
