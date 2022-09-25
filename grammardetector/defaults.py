# The default language model for spaCy's nlp
LANGUAGE_MODEL: str = "en_core_web_lg"


# The default format for INFO-level logs
LOGGER_FORMAT_BASIC: str = "[%(asctime)s] %(message)s"


# The default format for DEBUG-, WARN-, and ERROR-level logs
LOGGER_FORMAT_DETAILED: str = "[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s"


# The default log level
LOGGER_DEFAULT_LEVEL: int = 30


# The default patternset file extension type
PATTERN_SET_FILE_EXTENSION: str = "yaml"


# The default dirpath for the internal patternset files
PATTERN_SET_HOST_DIR: str = "patternsets"


# The default for patternset meta's best_match when undefined
PATTERN_SET_DEFAULT_BEST_MATCH: str = "longest"


# The default for patternset meta's how_many_matches when undefined
PATTERN_SET_DEFAULT_HOW_MANY_MATCHES: str = "all"
