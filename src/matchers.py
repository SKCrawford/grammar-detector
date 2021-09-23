import asyncio
import logging
from spacy.matcher import Matcher
from .extractors import get_doc
from .nlp import nlp
from .pattern import load_patternset
from .validators import is_not_type, is_truthy


logger = logging.getLogger(__name__)


async def match_by_pattern(pattern_filename, maybe_tokenized):
    ruleset = load_patternset(patternset_filename)
    matcher = _create_matcher(ruleset)
    return await _run_matcher(matcher, maybe_tokenized)


def _create_matcher(ruleset):
    matcher = Matcher(nlp.vocab, validate=True)
    for r in ruleset:
        matcher.add(r["rulename"], None, r["tokens"])
    return matcher


async def _run_matcher(matcher, maybe_tokenized):
    logger.debug(f"Validating matcher `{matcher}`")
    is_not_type(matcher, type(None))
    is_truthy(matcher)

    logger.debug(f"Tokenizing `{maybe_tokenized}`")
    doc = get_doc(maybe_tokenized)

    logger.debug("Running matcher")
    matches = matcher(doc)

    logger.debug(f"Grouping matches `{matches}`")
    grouped_matches = _group_matches_by_start(matches) # 2D list

    logger.debug(f"Getting the best matches in `{grouped_matches}`")
    best_matches = [_get_best_match(grouped_match) for grouped_match in grouped_matches]

    logger.debug(f"Parsing the best matches `{best_matches}`")
    parsed_best_matches = [_parse_match(best_match, doc) for best_match in best_matches]
    return parsed_best_matches


def _get_best_match(matches):
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


def _group_matches_by_start(matches):
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


def _parse_match(match, doc):
    logger.debug(f"Parsing match `{match}`")
    (match_id, start, end) = match
    rulename = nlp.vocab.strings[match_id]
    span = doc[start:end]
    return (rulename, span)
