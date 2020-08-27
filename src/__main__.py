import sys
from src.util.misc_tools import print_token_table
from .features.sentence_set.detector import detect_sentence_features


def main():
    sentences = []
    if len(sys.argv) > 0:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    count = 0
    for sentence in sentences:
        f_set = detect_sentence_features(sentence)

        if count:  # all lines after the 1st have whitespace between
            print()
        print(f"####### START SENTENCE {count} #######")
        print("##### Sentence tokens #####")
        print_token_table(sentence)
        print()
        print(f_set.toJSON())
        print(f"####### END SENTENCE {count} #######")
        count += 1


if __name__ == "__main__":
    main()
