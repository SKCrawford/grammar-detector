from logging import getLogger
from pprint import pformat
from sys import argv
from time import time
from .GrammarDetector import GrammarDetector
from .utils import token_table


def main() -> None:
    start_time: float = time()
    sentences: list[str] = []

    # Validate the input
    if len(argv) > 1:
        sentences = argv[1:]
    else:
        raise ValueError("No sentences were provided")

    # Create the detectors
    grammar_detector = GrammarDetector()
    logger = getLogger(__name__)

    # Run the detectors
    count: int = 0
    features = {}
    for sentence in sentences:
        logger.info(f"Sentence {count}: '{sentence}'")
        sentence_start_time: float = time()
        features = grammar_detector(sentence)
        print(grammar_detector.token_table(sentence))
        print(features)
        sentence_finish_time: float = time()
        count += 1

    finish_time: float = time()
    logger.info(f"Total run time: {finish_time - start_time:.2f}s")


if __name__ == "__main__":
    main()
