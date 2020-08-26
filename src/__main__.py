import sys
from src.util.misc_tools import print_token_table
from .features.sentence_set.detector import detect_sentence_features


def main():
    sentences = []
    if len(sys.argv) > 0:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    for sentence in sentences:
        print_token_table(sentence)
        f_set = detect_sentence_features(sentence)
        print(vars(f_set))
        print(vars(f_set.verb_features))
        print(vars(f_set.noun_features))

        count = 0
        for noun in f_set.noun_features.nouns:
            print(f"Noun {count}:", vars(noun))
            count += 1
        print()


if __name__ == "__main__":
    main()
