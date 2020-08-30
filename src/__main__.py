import logging
import sys
import src.logger
from src.util.misc_tools import to_token_table
from .features.sentence_set.detector import detect_sentence_features


logger = logging.getLogger(__name__)


def main():
    sentences = []
    if len(sys.argv) > 0:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    count = 0
    for sentence in sentences:
        logger.info(f"Sentences ({len(sentences)}): {sentences}")
        print(f"####### START SENTENCE {count} #######")
        logger.info(f"Sentence {count}: {sentence}")

        print("##### Sentence tokens #####")
        logger.info(f"Token table:\n{to_token_table(sentence)}")
        print(to_token_table(sentence), "\n")

        f_set = detect_sentence_features(sentence)
        logger.info(f"Sentence feature set:\n{f_set.toJSON()}")
        print(f_set.toJSON())
        print(f"####### END SENTENCE {count} #######")
        count += 1


if __name__ == "__main__":
    main()
