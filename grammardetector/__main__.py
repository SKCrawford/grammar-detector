from logging import getLogger
from pprint import pformat
from sys import argv
from .GrammarDetector import GrammarDetector
from .utils import Timekeeper, token_table


def main() -> None:
    tk = Timekeeper()
    tk.start("Total")
    sentences: list[str] = []

    # Validate the input
    if len(argv) > 1:
        sentences = argv[1:]
    else:
        raise ValueError("No sentences were provided")

    # Create the detectors
    tk.start("GrammarDetector init")
    grammar_detector = GrammarDetector(verbose=True)
    logger = getLogger(__name__)
    tk.stop("GrammarDetector init")

    # Run the detectors
    tk.start("Sentences")
    count: int = 0
    for sentence in sentences:
        print(f"Sentence {count}: '{sentence}'")
        tk.start(f"Sentence #{count}")
        features = grammar_detector(sentence)
        print(grammar_detector.token_table(sentence))
        print(features)
        tk.stop(f"Sentence #{count}")
        count += 1

    tk.stop("Sentences")
    tk.stop("Total")
    tk.report()


if __name__ == "__main__":
    main()
