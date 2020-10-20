import logging
from json import dumps


logger = logging.getLogger(__name__)


class Serializable:
    def to_JSON(self):
        logger.debug(f"Dumping JSON data for `{self}`")
        return dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)

    def set(self, key, value):
        setattr(self, key, value)
        return self

    def copy_dict(self, dict):
        self.__dict__ = dict.copy()
        return self
