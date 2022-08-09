from logging import getLogger
from os import listdir, path
from pprint import pformat
from sys import argv
from time import time
from .Config import Config
from .detectors import DetectorRepository
from .loaders import YamlLoader
from .logger import configure_logger
from .matches import Match
from .nlp import nlp
from .utils import Filepath, token_table


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

        self.config = Config(self.settings_path)
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
        # Logger
        log_level: int = self.config.prop_int("LOGGER_LEVEL")
        if self.very_verbose:
            log_level = 10
        elif self.verbose:
            log_level = 20
        configure_logger(self.config, log_level)

    def load(self):
        # Patternsets
        patternset_filepaths: list[str] = []
        feature_list: list[str] = []
        if not self.features == "all":
            feature_list = self.features.split(",")

        ## Internal patternsets
        if not self.exclude_builtin_patternsets:
            for fpath in Config().internal_patternset_filepaths:
                fp = Filepath(fpath)
                if not feature_list or fp.name in feature_list:
                    patternset_filepaths.append(fp.filepath)

        ## External patternsets
        if self.patternset_path:
            if path.isdir(self.patternset_path):
                for fpath in listdir(self.patternset_path):
                    fp = Filepath(fpath)
                    if not feature_list or fp.name in feature_list:
                        patternset_filepaths.append(fp.filepath)
            elif path.isfile(self.patternset_path):
                patternset_filepaths.append(self.patternset_path)
            else:
                msg = f"patternset_path expects a directory or file but got: '{self.patternset_path}"
                logger.error(msg)
                raise ValueError(msg)

        # Detectors
        [self.detector_repo.create(fpath) for fpath in patternset_filepaths]


def main() -> None:
    start_time: float = time()
    sentences: list[str] = []

    # Validate the input
    if len(argv) > 1:
        sentences = argv[1:]
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
    syndet.configure()
    syndet.load()
    logger = getLogger(__name__)

    # Run the detectors
    count: int = 0
    features = {}
    for sentence in sentences:
        feature_set = {}

        logger.info(f"Sentence {count}: '{sentence}'")
        sentence_start_time: float = time()

        table = token_table(nlp, sentence)
        logger.info(f"Token table:\n{table}")

        for detector in syndet.detectors:
            feature_set[detector.name] = detector(sentence)

        sentence_finish_time: float = time()
        features[sentence] = feature_set
        count += 1

    finish_time: float = time()
    logger.info(f"Total run time: {finish_time - start_time:.2f}s")

    logger.info("Detected features:")
    logger.info("\n" + pformat(features))


if __name__ == "__main__":
    main()
