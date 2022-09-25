from logging import getLogger
from os import listdir, path
from typing import Union
from .Config import Config
from .defaults import LANGUAGE_MODEL, LOGGER_DEFAULT_LEVEL
from .detectors import Detector, DetectorRepository, DetectorTester
from .logger import configure_logger
from .matches import Match
from .Nlp import Nlp
from .utils import Filepath, token_table


class GrammarDetector:
    """This class is the entrypoint for loading in patternset files and evaluating text input. It contains the `DetectorRepository` under the hood, which in turn contains the `Detectors`. By running `GrammarDetector.__call__(self, input: str)`, the text input will be compared against both the provided `patternsets` (via the `patternset_path` keyword argument) and the built-in `patternsets`. Extracting the `Detectors` from the `GrammarDetector` is possible via the `detectors: list[Detector]` property but unnecessary.

    Each resulting `Match` has two properties:
    1) `rulename`   -- (str) The name of the `Pattern` that best matches the input
    2) `span`       -- (str) The exact text that triggered the `Pattern`
    """

    def __init__(
        self,
        builtins: bool = True,
        language_model: str = LANGUAGE_MODEL,  # en_core_web_md
        patternset_path: str = "",
        verbose: bool = False,
        very_verbose: bool = False,
    ) -> None:
        """Create an instance of the `GrammarDetector`.

        Keyword arguments:
        builtins            -- (bool) If True, include built-in patternsets (default True)
        language_model      -- (str) The spaCy language_model used to create the global `nlp: Language` (default 'en_core_web_md')
        patternset_path     -- (str) A filepath or dirpath string pointing to a patternset or collection of patternsets (default '')
        verbose             -- (bool) If True, log INFO-level messages; `very_verbose` takes priority over `verbose` (default False)
        very_verbose        -- (bool) If True, log DEBUG-level messages; `very_verbose` takes priority over `verbose` (default False)
        """
        self._is_configured = False
        self._is_loaded = False

        self.builtins: bool = builtins
        self.language_model: str = language_model
        self.patternset_path: str = patternset_path
        self.verbose: bool = verbose
        self.very_verbose: bool = very_verbose

        self.config = Config()
        self.detector_repo = DetectorRepository()

        self._configure()
        self._load()

    def __call__(self, input: str) -> dict[str, Union[str, list[Match]]]:
        """Returns a dict of `Match`es after running all `Detectors` on the input string. One of the two ways to evaluate text for grammatical features. Use this `GrammarDetector.__call__()` method to evaluate text.

        Arguments:
        input -- (str) The sentence or chunk of text to be analyzed
        """
        matches: dict[str, Union[str, list[Match]]] = {}
        matches["input"] = input
        for detector in self.detectors:
            matches[detector.name] = detector(input)
        return matches

    @property
    def detectors(self) -> list[Detector]:
        """Returns all `Detectors`. One of the two ways to evaluate text for grammatical features. Use the `Detector.__call__` method to evaluate text."""
        if not self._is_loaded:
            raise RuntimeError(f"_load() must be called before accessing this property")
        return self.detector_repo.get_all()

    def _configure(self) -> None:
        """Configure the logger. Must be called before calling `_load()`."""
        log_level: int = LOGGER_DEFAULT_LEVEL
        if self.very_verbose:
            log_level = 10
        elif self.verbose:
            log_level = 20
        configure_logger(log_level)

        self.logger = getLogger(__name__)
        self._is_configured = True

    def _load(self) -> None:
        """Load the NLP and `PatternSets`. If the constructor's `builtins` is True, then the internal `PatternSets` provided with this class will be loaded. If the constructor's `patternset_path` is a valid filepath/dirpath string, then those `PatternSets` will also be loaded."""
        if not self._is_configured:
            raise RuntimeError(f"_configure() must be called before calling _load()")

        # NLP
        self.nlp = Nlp(self.language_model)

        # Patternsets
        patternset_filepaths: list[str] = []

        ## Internal patternsets
        if self.builtins:
            for fpath in Config().internal_patternset_filepaths:
                fp = Filepath(fpath)
                patternset_filepaths.append(fp.filepath)

        ## External patternsets
        if self.patternset_path:
            if path.isdir(self.patternset_path):
                for fpath in listdir(self.patternset_path):
                    fp = Filepath(f"{self.patternset_path}/{fpath}")
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

    def run_tests(self, builtin_tests: bool = False) -> None:
        tester = DetectorTester()
        results = []

        # Internal patternsets
        feature_names = [
            Filepath(fn).name for fn in self.config.internal_patternset_filenames
        ]

        for detector in self.detectors:
            if detector.name in feature_names:
                if builtin_tests:
                    results.append(tester.run_tests(detector))

            # External patternsets
            else:
                results.append(tester.run_tests(detector))

        if results:
            for name, num_pass, num_fail in results:
                print(f"{name} = PASS: {num_pass}, FAIL: {num_fail}")
        else:
            print("No tests found")

    def token_table(
        self,
        input: str,
        pos: bool = True,
        tag: bool = True,
        dependency: bool = True,
        lemma: bool = True,
    ) -> str:
        return token_table(
            self.nlp._nlp, input, pos=pos, tag=tag, dependency=dependency, lemma=lemma
        )
