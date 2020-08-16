import sys
from .features.core.detector import detect_features


def main():
    sentence = ""
    if len(sys.argv) > 1 and sys.argv[1]:
        sentence = sys.argv[1]
    else:
        sentence = "This will have been a test sentence."

    f_set = detect_features(sentence)
    print(vars(f_set))


if __name__ == "__main__":
    main()
