from logging import getLogger
from os import listdir, path
from typing import Union
from .Config import Config
from .detectors import Detector, DetectorRepository
from .logger import configure_logger
from .matches import Match
from .utils import Filepath


class GrammarDetector:
    """A class for detecting grammatical features in sentences, phrases, and clauses. The core of the detector is the YAML patternset files. These files contain a list of `Pattern`s with rulenames and tokens, meta configuration options, and unittests to evaluate the `Pattern`s. After constructing, configuring via `configure()`, and loading via `load()`, the `GrammarDetector` instance is ready to use. Does not currently support any text whose length is longer than a sentence.

        The two ways to evaluate the grammatical features of the sentence or chunk of text are:
        * Using the `__call__()` method to run all `Detector`s automatically
        * Using the `detectors` property and `Detector.__call__()` method to run the `Detector`s manually

        Each resulting `Match` has two properties:
        1) `rulename`   -- (str) The name of the `Pattern` that best matches the input
        2) `span`       -- (str) The exact text that triggered the `Pattern`
        """
    def __init__(
        self,
        dataset: str = "en_core_web_lg",
        builtins: bool = True,
        features: str = "all",
        patternset_path: str = "",
        settings_path: str = "settings.yaml",
        verbose: bool = False,
        very_verbose: bool = False,
    ) -> None:
        """Create an instance of the `GrammarDetector` by passing in configuration options. After construction, the methods `configure()` and `load()` must be called in order. After they have been called, the instance is ready to use.

        Keyword arguments:
        dataset                     -- (str) The spaCy dataset used to create the global `nlp: Language` (default 'en_core_web_lg')
        builtins -- (bool) If True, excludes patternsets included with the `GrammarDetector` (default False)
        features                    -- (str) A comma-separated string of features to select specific `Detector`s   (default 'all')
        patternset_path             -- (str) A filepath or dirpath string pointing to a patternset or collection of patternsets (default '')
        settings_path               -- (str) A filepath string pointing to a settings.yaml file, which contains the configuration options (default 'settings.yaml')
        verbose                     -- (bool) If True, log INFO-level messages; `very_verbose` takes priority over `verbose` (default False)
        very_verbose                -- (bool) If True, log DEBUG-level messages; `very_verbose` takes priority over `verbose` (default False)
        """
        self._is_configured = False
        self._is_loaded = False

        self.dataset: str = dataset
        self.builtins: bool = builtins
        self.features: str = features
        self.patternset_path: str = patternset_path
        self.settings_path: str = settings_path
        self.verbose: bool = verbose
        self.very_verbose: bool = very_verbose

        self.config = Config(self.settings_path)
        self.detector_repo = DetectorRepository()

    def __call__(self, input: str) -> dict[str, Union[str, list[Match]]]:
        """Returns a dict of `Match`es after running all `Detector`s on the input string. One of the two ways to evaluate text for grammatical features. Use this `GrammarDetector.__call__()` method to evaluate text. 

        Arguments:
        input -- The sentence or chunk of text to be analyze as a string
        """
        matches: dict[str, Union[str, list[Match]]]= {}
        matches["input"] = input
        for detector in self.detectors:
            matches[detector.name] = detector(input)
        return matches

    @property
    def detectors(self) -> list[Detector]:
        """Returns all `Detectors` created after calling `load`. One of the two ways to evaluate text for grammatical features. Use the `Detector.__call__` method to evaluate text."""
        if not self._is_loaded:
            raise RuntimeError(f"load() must be called before accessing this property")
        return self.detector_repo.get_all()

    def configure(self) -> None:
        """Configure the spaCy dataset and logger. Must be called before calling `load()`."""
        # TODO add support for configuring spaCy dataset

        # Logger
        log_level: int = self.config.prop_int("LOGGER_LEVEL")
        if self.very_verbose:
            log_level = 10
        elif self.verbose:
            log_level = 20
        configure_logger(self.config, log_level)

        self.logger = getLogger(__name__)
        self._is_configured = True

    def load(self) -> None:
        """Load the `PatternSet`s. If the constructor's `builtins` is True, then the internal `PatternSet`s provided with this class will be loaded. If the constructor's `patternset_path` is a valid filepath/dirpath string, then those `PatternSet`s will also be loaded."""
        if not self._is_configured:
            raise RuntimeError(f"configure() must be called before calling load()")

        # Patternsets
        patternset_filepaths: list[str] = []
        feature_list: list[str] = []
        if not self.features == "all":
            feature_list = self.features.split(",")

        ## Internal patternsets
        if self.builtins:
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
                self.logger.error(msg)
                raise ValueError(msg)

        # Detectors
        [self.detector_repo.create(fpath) for fpath in patternset_filepaths]
        self._is_loaded = True
