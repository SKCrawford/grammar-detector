import logging
from json import dumps


class Serializable:
    def toJSON(self):
        logger = logging.getLogger(self.toJSON.__name__)
        logger.debug(f"Started dumping JSON data for `{self}`")
        json = dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=2)
        logger.debug(f"Finished dumping JSON data for instance: `{json}`")
        return json
