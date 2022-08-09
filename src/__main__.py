from logging import getLogger
from pprint import pformat
from sys import argv
from time import time
from .SyntaxDetector import SyntaxDetector
from .nlp import nlp
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
    syndet = SyntaxDetector(
        exclude_builtin_patternsets=False,
        features="all",
        patternset_path="",
        pretty_print=True,
        settings_path="settings.yaml",
        verbose=True,
        very_verbose=False,
    )
    syndet.configure()
    syndet.load()
    logger = getLogger(__name__)

    # Run the detectors
    count: int = 0
    features = {}
    for sentence in sentences:
        logger.info(f"Sentence {count}: '{sentence}'")
        table = token_table(nlp, sentence)
        logger.info(f"Token table:\n{table}")

        sentence_start_time: float = time()
        features[sentence] = syndet(sentence)
        sentence_finish_time: float = time()
        count += 1

    finish_time: float = time()
    logger.info(f"Total run time: {finish_time - start_time:.2f}s")

    logger.info("Detected features:")
    if syndet.pretty_print:
        print(pformat(features))
    else:
        print(features)


if __name__ == "__main__":
    main()
