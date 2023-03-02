from logging import getLogger
from typing import Type
from ..loaders import FileLoader, YamlLoader
from ..patterns import PatternSet, PatternSetData, PatternSetRepository
from ..Repository import Repository
from ..utils import Filepath, singleton
from .Detector import Detector


logger = getLogger(__name__)


@singleton
class DetectorRepository(Repository):
    def __init__(self, file_loader: Type[FileLoader] = YamlLoader):
        super().__init__(Detector)
        self.file_loader = file_loader()
        self.pattern_set_repo = PatternSetRepository()

    def cache_key(self, pattern_set: PatternSet) -> str:
        return pattern_set.name

    def create(self, pattern_set_filepath: str) -> Detector:
        """Create and cache a Detector instance."""
        fp = Filepath(pattern_set_filepath)
        pset_data: PatternSetData = self.file_loader(fp.filepath)
        pattern_set: PatternSet = self.pattern_set_repo.create(fp.name, pset_data)
        stop_timer = self.tk.start(f"Create the '{pattern_set.name}' Detector")
        detector: Detector = super().create(pattern_set)
        stop_timer()
        return detector
