import logging
from src.util.spacy import get_doc, get_span


logger = logging.getLogger(__name__)


def detect_similarity(base_word, target_words):
    """Determine the similarity scores between a word and a list of words.
    Produces a list of tuples of shape (similarity_score, target_span, base_span).

    Given 0) a string, Span, or Doc and 1) a list of strings, Spans, or Docs,
    return a list of tuples of (float, Span, Span).
    """
    logger.debug("Started detecting")
    logger.debug(f"Comparing base word `{base_word}` to target words `{target_words}`")
    similarities = []
    base_span = get_span(base_word)
    for target_word in target_words:
        target_span = get_span(target_word)
        similarity = base_span.similarity(target_span)

        logger.debug(f"Similarity between `{base_word}` and `{target_word}` is `{similarity}`")
        entry = (similarity, target_span, base_span)
        similarities.append(entry)
    return similarities


def detect_similarities_between_verbs_and_nouns(verbs, nouns):
    """For each verb and noun, add an attribute called `similarities`,
    which holds the similarity scores relevant to each verb and noun.

    Immutable. Given a list and a list, return a tuple of (list, list).
    """
    # Immutably add the attribute "similarity" to each dict in the list
    verbs = [dict(verb, **{ "similarities": [] }) for verb in list.copy(verbs)]
    nouns = [dict(noun, **{ "similarities": [] }) for noun in list.copy(nouns)]

    for verb in verbs:
        entries = detect_similarity(verb["span"], [noun["span"] for noun in nouns])
        noun_i = 0 # The order of nouns matches the order of similarity entries
        for entry in entries:
            verb["similarities"].append(entry)
            nouns[noun_i]["similarities"].append(entry)
            noun_i += 1
    return (verbs, nouns)
