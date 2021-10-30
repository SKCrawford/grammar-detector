import asyncio
import pprint
import sys
import time
import src.logger
from logging import getLogger
from settings import pattern_set_config
from .detectors import detect_feature
from .utils import to_token_table
from .nlp import nlp


logger = getLogger(__name__)


async def main() -> None:
    start_time: float = time.time()
    sentences: list[str] = []

    if len(sys.argv) > 1:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    count: int = 0
    for sentence in sentences:
        sentence_start_time: float = time.time()

        logger.info(f"Sentences ({len(sentences)}): {sentences}")
        logger.info(f"Sentence {count}: '{sentence}'")

        token_table = to_token_table(nlp, sentence)
        logger.info(f"Token table:\n{token_table}")

        feature_set = {}
        for feature in pattern_set_config.names:
            result = detect_feature(sentence, feature)
            feature_set[feature] = result

        logger.info("Detected features:")
        logger.info("\n" + pprint.pformat(feature_set))

        sentence_finish_time: float = time.time()
        logger.info(
            f"Sentence run time: {sentence_finish_time - sentence_start_time:.2f}s"
        )
        count += 1
    finish_time: float = time.time()
    logger.info(f"Total run time: {finish_time - start_time:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
