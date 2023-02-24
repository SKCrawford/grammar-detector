from logging import getLogger
from spacy import explain
from spacy.language import Language
from tabulate import tabulate


logger = getLogger(__name__)


def token_table(
    nlp: Language,
    sentence: str,
    pos: bool = True,
    tag: bool = True,
    dependency: bool = True,
    lemma: bool = True,
) -> str:
    """Generate a table containing the parts-of-speech, tag, dependency, and lemma of each token. This is helpful for visualizing token sequences.

    Keyword arguments:
    input       -- (str) The sentence or chunk of text to be analyzed
    pos         -- (bool) If True, include the part-of-speech property (default True)
    tag         -- (bool) If True, include the tag property (default True)
    dependency  -- (bool) If True, include the dependency property (default True)
    lemma       -- (bool) If True, include the lemma property (default True)
    """
    logger.debug(f"Creating the token table for `{sentence}`")

    logger.debug("Creating the table headers")
    headers = []
    headers.append("Word")
    if pos:
        headers.append("POS")
        headers.append("POS Definition")
    if tag:
        headers.append("Tag")
        headers.append("Tag Definition")
    if dependency:
        headers.append("Dep.")
        headers.append("Dep. Definition")
    if lemma:
        headers.append("Lemma.")

    logger.debug("Tokenizing")
    tagged_words = nlp(sentence)

    logger.debug("Extracting the features")
    data = []
    for word in tagged_words:
        entry = []
        entry.append(word.text)
        if pos:
            entry.append(word.pos_)
            entry.append(explain(word.pos_))  # type: ignore # explain is untyped
        if tag:
            entry.append(word.tag_)
            entry.append(explain(word.tag_))  # type: ignore # explain is untyped
        if dependency:
            entry.append(word.dep_)
            entry.append(explain(word.dep_))  # type: ignore # explain is untyped
        if lemma:
            entry.append(word.lemma_)
        data.append(entry)
    logger.debug("Returning the token table")
    return tabulate(data, headers=headers, tablefmt="github")
