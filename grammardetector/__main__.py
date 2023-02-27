from logging import getLogger
from pprint import pformat
from sys import argv
from .GrammarDetector import GrammarDetector
from .utils import Timekeeper, token_table


def main() -> None:
    is_verbose: bool = False

    tk = Timekeeper()
    stop_timer_total = tk.start("Total")

    # Validate the input
    sentences: list[str] = []
    if len(argv) > 1:
        sentences = argv[1:]
    else:
        raise ValueError("No sentences were provided")

    # Create the detectors
    grammar_detector = GrammarDetector(verbose=is_verbose)
    logger = getLogger(__name__)

    # Run the detectors
    stop_timer_all_sent = tk.start("Sentences")
    results = []
    for count, sentence in enumerate(sentences):
        stop_timer = tk.start(f"Sentence #{count}")
        features = grammar_detector(sentence)
        table = grammar_detector.token_table(sentence)
        results.append((features, table))
        stop_timer()

    stop_timer_all_sent()
    stop_timer_total()

    if grammar_detector.verbose or grammar_detector.very_verbose:
        tk.report(sort_by="started_at")

    if results:
        for features, table in results:
            print(table)
            print(features)


if __name__ == "__main__":
    main()
