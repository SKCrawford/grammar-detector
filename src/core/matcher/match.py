import asyncio
import logging
from spacy.matcher import Matcher
from src.nlp import nlp
from src.util.spacy import get_doc
from src.util.validator import is_not_type, is_truthy
from ..pattern import load_patterns
from .parse import get_best_match, group_matches_by_start, parse_match


logger = logging.getLogger(__name__)


def create_matcher(ruleset):
    matcher = Matcher(nlp.vocab, validate=True)
    for r in ruleset:
        matcher.add(r["rulename"], None, r["tokens"])
    return matcher


async def run_matcher(matcher, maybe_tokenized):
    logger.debug(f"Validating matcher `{matcher}`")
    is_not_type(matcher, type(None))
    is_truthy(matcher)

    logger.debug(f"Tokenizing `{maybe_tokenized}`")
    doc = get_doc(maybe_tokenized)

    logger.debug("Running matcher")
    matches = matcher(doc)

    logger.debug(f"Grouping matches `{matches}`")
    grouped_matches = group_matches_by_start(matches) # 2D list

    logger.debug(f"Getting the best matches in `{grouped_matches}`")
    best_matches = [get_best_match(grouped_match) for grouped_match in grouped_matches]

    logger.debug(f"Parsing the best matches `{best_matches}`")
    parsed_best_matches = [parse_match(best_match, doc) for best_match in best_matches]
    return parsed_best_matches


async def match_by_pattern(pattern_filename, maybe_tokenized):
    ruleset = load_patterns(pattern_filename)
    matcher = create_matcher(ruleset)
    return await run_matcher(matcher, maybe_tokenized)
