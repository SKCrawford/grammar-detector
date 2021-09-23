import asyncio
import logging
import pprint
import sys
import time
import src.logger
from .detectors import detect_features
from .utils import to_token_table


logger = logging.getLogger(__name__)


async def main():
    start_time = time.time()
    sentences = []
    if len(sys.argv) > 0:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    count = 0
    for sentence in sentences:
        sentence_start_time = time.time()
        logger.info(f"Sentences ({len(sentences)}): `{sentences}`")
        print(f"####### START SENTENCE {count} #######")
        logger.info(f"Sentence {count}: `{sentence}`")

        print("##### Sentence tokens #####")
        token_table = to_token_table(sentence)
        logger.info(f"Token table:\n{token_table}")
        print(token_table, "\n")

        feature_set = await detect_features(sentence)
        logger.info("Detected features:")
        logger.info(pprint.pformat(feature_set))
        pprint.pprint(feature_set)
        print(f"Sentence run time: {time.time() - sentence_start_time:.2f}s")
        print(f"####### END SENTENCE {count} #######")
        count += 1
    print(f"Total run time: {time.time() - start_time:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
