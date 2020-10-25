import logging
import pprint
import sys
import src.logger
from src.util.misc_tools import to_token_table
from .features import detect_features


logger = logging.getLogger(__name__)


def main():
    sentences = []
    if len(sys.argv) > 0:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    count = 0
    for sentence in sentences:
        logger.info(f"Sentences ({len(sentences)}): `{sentences}`")
        print(f"####### START SENTENCE {count} #######")
        logger.info(f"Sentence {count}: `{sentence}`")

        print("##### Sentence tokens #####")
        token_table = to_token_table(sentence)
        logger.info(f"Token table:\n{token_table}")
        print(token_table, "\n")

        feature_set = detect_features(sentence)
        logger.info("Detected features:")
        logger.info(pprint.pformat(feature_set))
        pprint.pprint(feature_set)
        print(f"####### END SENTENCE {count} #######")
        count += 1


if __name__ == "__main__":
    main()
