import os
import pprint
import sys
import time
from logging import getLogger
from settings import configure_settings, Filepath
from .detectors import DetectorRepository
from .loaders import YamlLoader
from .logger import configure_logger
from .matches import Match
from .nlp import nlp
from .utils import to_token_table
from .config import Config


class SyntaxDetector:
    def __init__(
        self,
        dataset: str = "en_core_web_lg",
        exclude_builtin_patternsets: bool = False,
        features: str = "all",
        patternset_path: str = "",
        settings_path: str = "settings.yaml",
        verbose: bool = True,
        very_verbose: bool = False,
    ) -> None:
        self.dataset: str = dataset
        self.exclude_builtin_patternsets: bool = exclude_builtin_patternsets
        self.features: str = features
        self.patternset_path: str = patternset_path
        self.settings_path: str = settings_path
        self.verbose: bool = verbose
        self.very_verbose: bool = very_verbose
        self.detector_repo = DetectorRepository()

    def __call__(self, input: str) -> dict[str, list[Match]]:
        matches: dict[str, list[Match]] = {}
        for detector in self.detectors:
            matches[detector.name] = detector(input)
        return matches

    @property
    def detectors(self):
        return self.detector_repo.get_all()

    def configure(self):
        config = Config(self.settings_path)

        # Logger
        log_level: int = logger_conf.prop_int("LEVEL")
        if self.very_verbose:
            log_level = 10
        elif self.verbose:
            log_level = 20
        configure_logger(logger_conf, log_level)

    def load(self):
        # Patternsets
        patternset_filepaths: list[str] = []
        feature_list: list[str] = []
        if not features == "all":
            feature_list = self.features.split(",")

        ## Internal patternsets
        if not exclude_builtin_patternsets:
            for fpath in patternset_conf.internal_patternset_filepaths:
                fp = Filepath(fpath)
                if not feature_list or fp.name in feature_list:
                    patternset_filepaths.append(fp.filepath)

        ## External patternsets
        if patternset_path:
            if os.path.isdir(patternset_path):
                for fpath in os.listdir(patternset_path):
                    fp = Filepath(fpath)
                    if not feature_list or fp.name in feature_list:
                        patternset_filepaths.append(fp.filepath)
            elif os.path.isfile(patternset_path):
                patternset_filepaths.append(patternset_path)
            else:
                msg = f"patternset_path expects a directory or file but got: '{patternset_path}"
                logger.error(msg)
                raise ValueError(msg)

        # Detectors
        [self.detector_repo.create(fpath) for fpath in patternset_filepaths]


def main() -> None:
    start_time: float = time.time()
    sentences: list[str] = []

    # Validate the input
    if len(sys.argv) > 1:
        sentences = sys.argv[1:]
    else:
        raise ValueError("No sentences were provided")

    # Create the detectors
    syndet = SyntaxDetector(
        exclude_builtin_patternsets=False,
        features="all",
        patternset_path="",
        settings_path="settings.yaml",
        verbose=True,
        very_verbose=False,
    )

    # Run the detectors
    count: int = 0
    features = {}
    for sentence in sentences:
        feature_set = {}

        logger.info(f"Sentence {count}: '{sentence}'")
        sentence_start_time: float = time.time()

        # token_table = to_token_table(syndet.nlp, sentence)
        token_table = to_token_table(nlp, sentence)
        logger.info(f"Token table:\n{token_table}")

        for detector in syndet.detectors:
            feature_set[detector.name] = detector(sentence)

        sentence_finish_time: float = time.time()
        features[sentence] = feature_set
        count += 1

    finish_time: float = time.time()
    logger.info(f"Total run time: {finish_time - start_time:.2f}s")

    logger.info("Detected features:")
    logger.info("\n" + pprint.pformat(features))


if __name__ == "__main__":
    main()
