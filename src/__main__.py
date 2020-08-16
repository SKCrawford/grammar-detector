from .features.verb_tense.detector import detect_verb_tense
import sys


def main():
    sentence = sys.argv[1]
    verb_tense = detect_verb_tense(sentence)
    print(verb_tense)


if __name__ == "__main__":
    main()
