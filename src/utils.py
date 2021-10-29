from functools import reduce, wraps
from logging import getLogger
from operator import concat
from spacy import explain
from spacy.language import Language
from spacy.tokens import Doc, Span
from typing import Union
from tabulate import tabulate


Doclike = Union[Doc, Span]


logger = getLogger(__name__)


def singleton(klass):
    instances = []

    @wraps(klass.__new__)
    def singleton_wrapper(*args, **kwargs):
        if not instances:
            logger.debug("Constructing a new instance singleton")
            instance = klass(*args, **kwargs)
            instances.append(instance)
        else:
            logger.debug("Retrieving an existing instance singleton")
        return instances[0]

    return singleton_wrapper


# Source: https://stackoverflow.com/a/45323085
def flatten(a):
    return reduce(concat, a)


def is_hidden_file(filename: str) -> bool:
    """Returns True if a file's filename indicates whether it is a hidden filename. Otherwise, returns False."""
    return bool(str(filename).startswith("."))


def has_extension(expected_extension: str, filename: str) -> bool:
    """Returns True if a file's filename ends with the expected extension. Otherwise, returns False."""
    return bool(str(filename).endswith(expected_extension))


def trim_extension(extension: str, filename: str) -> str:
    return filename.replace(extension, "")


def to_token_table(
    nlp: Language,
    sentence: str,
    pos: bool = True,
    tag: bool = True,
    dependency: bool = True,
    lemma: bool = True,
) -> str:
    """Print the linguistics features of each word in a sentence.
    If pos is True, then print the part-of-speech (POS). Defaults to True.
    If tag is True, then print the tag. Defaults to True.
    If dependency is True, then print the dependencices. Defaults to True.
    If lemma is True, then print the lemma. Defaults to True.
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
