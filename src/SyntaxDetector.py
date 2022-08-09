from os import listdir, path
from pprint import pformat
from .Config import Config
from .detectors import DetectorRepository
from .logger import configure_logger
from .matches import Match
from .utils import Filepath


class SyntaxDetector:
    def __init__(
        self,
        dataset: str = "en_core_web_lg",
        exclude_builtin_patternsets: bool = False,
        features: str = "all",
        patternset_path: str = "",
        pretty_print: bool = False,
        settings_path: str = "settings.yaml",
        verbose: bool = False,
        very_verbose: bool = False,
    ) -> None:
        self.dataset: str = dataset
        self.exclude_builtin_patternsets: bool = exclude_builtin_patternsets
        self.features: str = features
        self.patternset_path: str = patternset_path
        self.pretty_print: bool = pretty_print
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
