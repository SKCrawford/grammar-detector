import asyncio
import pprint
import sys
import time
import src.logger
from logging import getLogger
from settings import pattern_set_config
from .detectors import DetectorRepository
from .loaders import YamlLoader
from .nlp import nlp
from .patterns import PatternSetRepository
from .utils import to_token_table


logger = getLogger(__name__)


async def main() -> None:
    start_time: float = time.time()
    sentences: list[str] = []

    # Validate the input
    if len(sys.argv) > 1:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    # Load the internal patternsets
    detector_repo = DetectorRepository(file_loader=YamlLoader)
    for internal_pset_fpath in pattern_set_config.internal_patternset_filepaths:
        detector_repo.create(internal_pset_fpath)

    # Run the detectors
    feature_set = {}
    count: int = 0
    for sentence in sentences:
        logger.info(f"Sentence {count}: '{sentence}'")
        sentence_start_time: float = time.time()

        token_table = to_token_table(nlp, sentence)
        logger.info(f"Token table:\n{token_table}")

        for detector in detector_repo.get_all():
            feature_set[detector.name] = detector(sentence)

        sentence_finish_time: float = time.time()
        count += 1

    finish_time: float = time.time()
    logger.info(f"Total run time: {finish_time - start_time:.2f}s")

    logger.info("Detected features:")
    logger.info("\n" + pprint.pformat(feature_set))


if __name__ == "__main__":
    asyncio.run(main())
