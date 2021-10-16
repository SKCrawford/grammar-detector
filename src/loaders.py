from logging import getLogger
from os.path import join
from typing import Any, TextIO
from yaml import FullLoader, load as load_yaml
from .patterns import PatternSet


logger = getLogger(__name__)


class FileLoader:
    def __init__(self, file_ext: str, dir_path: str) -> None:
        if not file_ext:
            msg = f"argument 'file_ext' is missing"
            logger.error(msg)
            raise ValueError(msg)
        if not dir_path:
            msg = f"argument 'dir_path' is missing"
            logger.error(msg)
            raise ValueError(msg)

        self.file_ext = file_ext
        self.dir_path = dir_path

    def __call__(self, filename_base: str) -> dict[str, Any]:
        path: str = self.generate_path(filename_base)
        with open(path, "r") as file:
            return self.load(file)

    def generate_path(self, filename_base: str) -> str:
        return join(self.dir_path, f"{filename_base}.{self.file_ext}")

    def load(self, file: TextIO) -> dict[str, Any]:
        msg = f"FileLoader.load was not implemented"
        logger.error(msg)
        raise NotImplementedError(msg)


class YamlLoader(FileLoader):
    def __init__(self, *args: str, **kwargs: str) -> None:
        # type(*args) == the type of one of the values in its list
        # type(**kwargs) == the type of one of the values of its key-value pairs
        super().__init__("yaml", *args, **kwargs)

    def load(self, file: TextIO) -> Any:
        return load_yaml(file, Loader=FullLoader)


class PatternSetLoader:
    """FileLoader is injected, not inherited."""

    def __init__(self, file_loader: FileLoader) -> None:
        self.file_loader = file_loader
        self.pattern_sets: dict[str, PatternSet] = {}

    def __call__(self, pset_name: str) -> PatternSet:
        if pset_name in self.pattern_sets:
            logger.debug(f"Retrieving patternset '{pset_name}'")
            return self.pattern_sets[pset_name]

        logger.debug(f"Loading patternset '{pset_name}'")
        pset_data = self.file_loader(pset_name)
        pset = PatternSet(pset_name, pset_data)
        self.pattern_sets[pset.name] = pset
        return pset
