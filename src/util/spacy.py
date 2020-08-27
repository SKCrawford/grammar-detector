from spacy.tokens import Doc, Span
from src.nlp import nlp
from .validator import is_not_type, is_truthy, is_type


def get_best_match(matches):
    is_type(matches, list)
    is_truthy(matches)
    
    all_starts = [start for (_, start, _) in matches]
    starts_are_identical = len(set(all_starts)) < 2
    if not starts_are_identical:
        raise ValueError(f"expected a list of Matches with identical start values")
    return matches.pop()


def get_best_matches(match_groups):
    return [get_best_match(matches) for matches in match_groups]


def group_matches_by_start(matches):
    """Given a list of Matches, return a 2D list of Matches. O(n)."""
    match_groups = []
    i = -1 
    last_start = None
    for match in matches:
        (match_id, start, end) = match
        if start is not last_start:
            last_start = start 
            i += 1
            match_groups.append([])
        match_groups[i].append(match)
    return match_groups


def is_tokenized(maybe_tokenized):
    is_not_type(maybe_tokenized, type(None))
    is_truthy(maybe_tokenized)
    if isinstance(maybe_tokenized, str):
        return False
    elif isinstance(maybe_tokenized, Doc) or isinstance(maybe_tokenized, Span):
        return True
    else:
        raise TypeError(f"expected a string, Doc, or Span but got {type(maybe_tokenized)}")


def make_doc(maybe_tokenized):
    """Given a string, Doc, or Span, return a Doc."""
    return nlp(maybe_tokenized) if not is_tokenized(maybe_tokenized) else maybe_tokenized


def parse_match(match, doc):
    (match_id, start, end) = match
    rulename = nlp.vocab.strings[match_id]
    span = doc[start:end]
    return (rulename, span)


def run_matcher(matcher, maybe_tokenized):
    is_not_type(matcher, type(None))
    is_truthy(matcher)
    doc = make_doc(maybe_tokenized)
    matches = matcher(doc)
    grouped_matches = group_matches_by_start(matches) # 2D list
    best_matches = get_best_matches(grouped_matches)
    return [parse_match(best_match, doc) for best_match in best_matches]
