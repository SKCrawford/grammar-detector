import asyncio
import logging
from .noun_set import detect_noun_features
from .similarity import detect_similarities_between_verbs_and_nouns
from .verb_set import detect_verb_features


logger = logging.getLogger(__name__)


async def detect_features(sentence):
    """The main entry point for the feature detector."""
    logger.debug("Started detecting")
    nouns, verbs = await asyncio.gather(
        detect_noun_features(sentence),
        detect_verb_features(sentence)
    )
    (verbs, nouns) = await detect_similarities_between_verbs_and_nouns(verbs, nouns)

    feature_set = {}
    feature_set["sentence"] = sentence
    feature_set["nouns"] = nouns
    feature_set["verbs"] = verbs
    return feature_set
