import logging
from spacy.tokens import Doc, Span
from src.nlp import nlp
from src.util.validator import is_not_type, is_truthy, is_type


logger = logging.getLogger(__name__)


def get_best_match(matches):
    logger.debug(f"Validating matches `{matches}`")
    is_type(matches, list)
    is_truthy(matches)

    all_starts = [start for (_, start, _) in matches]
    starts_are_identical = len(set(all_starts)) < 2
    if not starts_are_identical:
        err_msg = f"Expected a list of Matches with identical start values but got `{all_starts}`"
        logger.error(err_msg)
        raise ValueError(err_msg)

    logger.debug("Determining the best match")
    match = matches.pop() # This will probably cause problems one day
    return match


def group_matches_by_start(matches):
    """Given a list of Matches, return a 2D list of Matches. O(n)."""

    match_groups = []
    i = -1 
    last_start = None
    logger.debug(f"Grouping matches `{matches}`")
    for match in matches:
        (match_id, start, end) = match
        if start is not last_start:
            logger.debug(f"Creating group for start `{start}`")
            last_start = start 
            i += 1
            match_groups.append([])
        match_groups[i].append(match)
    return match_groups


def parse_match(match, doc):
    logger.debug(f"Parsing match `{match}`")
    (match_id, start, end) = match
    rulename = nlp.vocab.strings[match_id]
    span = doc[start:end]
    return (rulename, span)
