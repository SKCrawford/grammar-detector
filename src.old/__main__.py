import asyncio
import pprint
import sys
import time
import src.logger
from logging import getLogger
from settings import pattern_set_config
from .detectors import detect_features
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
        logger.info(f"Sentences ({len(sentences)}): `{sentences}`")
        print(f"####### START SENTENCE {count} #######")
        logger.info(f"Sentence {count}: `{sentence}`")

        print("##### Sentence tokens #####")
        token_table = to_token_table(nlp, sentence)
        logger.info(f"Token table:\n{token_table}")
        print(token_table, "\n")

        feature_set = await detect_features(sentence, pattern_set_config.names)

        logger.info("Detected features:")
        logger.info(pprint.pformat(feature_set))
        print("Detected features:")
        pprint.pprint(feature_set)
        print(f"Sentence run time: {time.time() - sentence_start_time:.2f}s")
        print(f"####### END SENTENCE {count} #######")
        count += 1
    print(f"Total run time: {time.time() - start_time:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
