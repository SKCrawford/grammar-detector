import sys
from .features.sentence_set.detector import detect_sentence_features


def main():
    sentence = ""
    if len(sys.argv) > 1 and sys.argv[1]:
        sentence = sys.argv[1]
    else:
        sentence = "I am a test."

    f_set = detect_sentence_features(sentence)
    print(vars(f_set))


if __name__ == "__main__":
    main()
