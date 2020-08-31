import logging
from spacy.tokens import Doc, Span
from src.nlp import nlp
from .validator import is_not_type, is_truthy, is_type


def get_best_match(matches):
    logger = logging.getLogger(get_best_match.__name__)
    logger.debug(f"Started validating matches: `{matches}`")
    is_type(matches, list)
    is_truthy(matches)

    all_starts = [start for (_, start, _) in matches]
    starts_are_identical = len(set(all_starts)) < 2
    if not starts_are_identical:
        err_msg = "Expected a list of Matches with identical start values"
        logger.error(err_msg)
        raise ValueError(err_msg)

    logger.debug("Finished validating matches")
    logger.debug(f"Started determining the best match: `{matches}`")
    match = matches.pop()
    logger.debug(f"Finished determining the best match: `{match}`")
    return match


def get_best_matches(match_groups):
    logger = logging.getLogger(get_best_matches.__name__)
    logger.debug(f"Started determining the best match for each group: {match_groups}")
    best_matches = [get_best_match(matches) for matches in match_groups]
    logger.debug(f"Finished determining the best match for each group: {best_matches}")
    return best_matches



def group_matches_by_start(matches):
    """Given a list of Matches, return a 2D list of Matches. O(n)."""
    logger = logging.getLogger(group_matches_by_start.__name__)

    match_groups = []
    i = -1 
    last_start = None
    logger.debug(f"Started grouping matches: `{matches}`")
    for match in matches:
        (match_id, start, end) = match
        if start is not last_start:
            last_start = start 
            i += 1
            match_groups.append([])
        match_groups[i].append(match)
    logger.debug(f"Finished grouping matches: `{match_groups}`")
    return match_groups


def is_tokenized(maybe_tokenized):
    logger = logging.getLogger(is_tokenized.__name__)
    logger.debug(f"Started validating input: {maybe_tokenized}")
    is_not_type(maybe_tokenized, type(None))
    is_truthy(maybe_tokenized)
    logger.debug("Finished validating input")
    logger.debug("Started determining if input is already tokenized")
    if isinstance(maybe_tokenized, str):
        logger.debug("Finished determining if input is already tokenized")
        logger.debug("Sentence is not tokenized, so returning False")
        return False
    elif isinstance(maybe_tokenized, Doc) or isinstance(maybe_tokenized, Span):
        logger.debug("Finished determining if input is already tokenized")
        logger.debug("Sentence is already tokenized, so returning True")
        return True
    err_msg = f"Expected a string, Doc, or Span but got `{type(maybe_tokenized)}`"
    logger.error(err_msg)
    raise TypeError(err_msg)


def make_doc(maybe_tokenized):
    """Given a string, Doc, or Span, return a Doc."""
    logger = logging.getLogger(make_doc.__name__)
    logger.debug(f"Started tokenizing `{maybe_tokenized}`")
    doc = nlp(maybe_tokenized) if not is_tokenized(maybe_tokenized) else maybe_tokenized
    logger.debug(f"Finished tokenizing: `{doc}`")
    return doc


def parse_match(match, doc):
    logger = logging.getLogger(parse_match.__name__)
    logger.debug(f"Started parsing match: `{match}`")
    (match_id, start, end) = match
    rulename = nlp.vocab.strings[match_id]
    span = doc[start:end]
    logger.debug(f"Finished parsing match: `{rulename}`, `{span}`")
    return (rulename, span)


def run_matcher(matcher, maybe_tokenized):
    logger = logging.getLogger(run_matcher.__name__)
    logger.debug(f"Started validating matcher: `{matcher}`")
    is_not_type(matcher, type(None))
    is_truthy(matcher)
    logger.debug(f"Finished validating matcher")
    logger.debug(f"Started tokenizing the input: `{input}`")
    doc = make_doc(maybe_tokenized)
    logger.debug(f"Finished tokenizing the input: `{doc}`")

    logger.debug("Started running matcher on doc")
    matches = matcher(doc)
    logger.debug(f"Finished running matcher: `{matches}`")

    logger.debug(f"Started grouping matches: `{matches}`")
    grouped_matches = group_matches_by_start(matches) # 2D list
    logger.debug(f"Finished grouping matches: `{grouped_matches}`")

    logger.debug(f"Started getting the best matches: `{grouped_matches}`")
    best_matches = get_best_matches(grouped_matches)
    logger.debug(f"Finished getting the best matches: `{best_matches}`")

    logger.debug(f"Started parsing the best matches: `{best_matches}`")
    parsed_best_matches = [parse_match(best_match, doc) for best_match in best_matches]
    logger.debug(f"Finished parsing the best matches: `{parsed_best_matches}`")
    return parsed_best_matches
