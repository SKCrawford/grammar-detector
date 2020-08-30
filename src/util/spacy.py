import logging
from spacy.tokens import Doc, Span
from src.nlp import nlp
from .validator import is_not_type, is_truthy, is_type


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


def get_best_matches(match_groups):
    logger.debug(f"Determining the best match for each group in `{match_groups}`")
    best_matches = [get_best_match(matches) for matches in match_groups]
    return best_matches



def group_matches_by_start(matches):
    """Given a list of Matches, return a 2D list of Matches. O(n)."""

    match_groups = []
    i = -1 
    last_start = None
    logger.debug(f"Grouping matches `{matches}`")
    for match in matches:
        (match_id, start, end) = match
        logger.debug(f"Creating group for start `{start}`")
        if start is not last_start:
            last_start = start 
            i += 1
            match_groups.append([])
        match_groups[i].append(match)
    return match_groups


def is_tokenized(maybe_tokenized):
    logger.debug(f"Validating `{maybe_tokenized}`")
    is_not_type(maybe_tokenized, type(None))
    is_truthy(maybe_tokenized)
    logger.debug("Determining if input is already tokenized")
    if isinstance(maybe_tokenized, str):
        logger.debug("Sentence is not tokenized, so returning False")
        return False
    elif isinstance(maybe_tokenized, Doc) or isinstance(maybe_tokenized, Span):
        logger.debug("Sentence is already tokenized, so returning True")
        return True
    err_msg = f"Expected a string, Doc, or Span but got `{type(maybe_tokenized)}`"
    logger.error(err_msg)
    raise TypeError(err_msg)


def make_doc(maybe_tokenized):
    """Given a string, Doc, or Span, return a Doc."""
    logger.debug(f"Tokenizing `{maybe_tokenized}`")
    return nlp(maybe_tokenized) if not is_tokenized(maybe_tokenized) else maybe_tokenized


def parse_match(match, doc):
    logger.debug(f"Parsing match `{match}`")
    (match_id, start, end) = match
    rulename = nlp.vocab.strings[match_id]
    span = doc[start:end]
    return (rulename, span)


def run_matcher(matcher, maybe_tokenized):
    logger.debug(f"Validating matcher `{matcher}`")
    is_not_type(matcher, type(None))
    is_truthy(matcher)
    logger.debug(f"Tokenizing `{maybe_tokenized}`")
    doc = make_doc(maybe_tokenized)

    logger.debug("Running matcher")
    matches = matcher(doc)

    logger.debug(f"Grouping matches `{matches}`")
    grouped_matches = group_matches_by_start(matches) # 2D list

    logger.debug(f"Getting the best matches in `{grouped_matches}`")
    best_matches = get_best_matches(grouped_matches)

    logger.debug(f"Parsing the best matches `{best_matches}`")
    parsed_best_matches = [parse_match(best_match, doc) for best_match in best_matches]
    return parsed_best_matches
