import logging
from json import dumps


logger = logging.getLogger(__name__)


class Serializable:
    def toJSON(self):
        logger.debug(f"Dumping JSON data for `{self}`")
        json = dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=2)
        return json
