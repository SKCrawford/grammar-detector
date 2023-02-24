from logging import getLogger
from spacy import explain
from spacy.language import Language
from tabulate import tabulate
from typing import Literal


logger = getLogger(__name__)


TokenlikeKeys = Literal["pos", "tag", "dep", "lemma", "word"]
Tokenlike = dict[TokenlikeKeys, str]


def token_data(
    nlp: Language,
    sentence: str,
    pos: bool = True,
    tag: bool = True,
    dependency: bool = True,
    lemma: bool = False,
    word: bool = False,
) -> list[Tokenlike]:
    """Generate a list of objects containing the parts-of-speech, tags, dependencies, and lemmas of each token. This is particularly helpful for writing new patterns.

    Keyword arguments:
    nlp         -- (Language) The `nlp` instance
    input       -- (str) The sentence or chunk of text to be analyzed
    pos         -- (bool) If True, include the part-of-speech property (default True)
    tag         -- (bool) If True, include the tag property (default True)
    dependency  -- (bool) If True, include the dependency property (default True)
    lemma       -- (bool) If True, include the lemma property (default False)
    word        -- (bool) If True, include the word itself (default False)
    """
    logger.debug(f"Extracting the token data for `{sentence}`")

    logger.debug("Tokenizing")
    tagged_words = nlp(sentence)

    logger.debug("Extracting")
    data: list[Tokenlike] = []
    for tagged_word in tagged_words:
        entry: Tokenlike = {}
        if pos:
            entry["pos"] = tagged_word.pos_
        if tag:
            entry["tag"] = tagged_word.tag_
        if dependency:
            entry["dep"] = tagged_word.dep_
        if lemma:
            entry["lemma"] = tagged_word.lemma_
        if word:
            entry["word"] = tagged_word.text
        data.append(entry)
    logger.debug("Returning the token data")
    return data
