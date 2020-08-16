import json
import os
from src.enums.TenseAspect import TenseAspect
from ..core.model.PatternSet import PatternSet



def load_patterns():
    json_path = f"{os.path.dirname(__file__)}/../../../patterns.json"
    with open(json_path, "r") as f:
        return json.load(f)


Patterns = load_patterns()


def create_verb_tense_pattern_set():
    tense_aspects = Patterns["tense_aspects"]
    p_set = PatternSet("verb tenses")
    for name in tense_aspects:
        tokens = tense_aspects[name]
        p_set.create(name, tokens)
    return p_set


verb_tense_pattern_set = create_verb_tense_pattern_set()
