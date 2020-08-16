from src.enums import *
from src.utils import is_enum_member


class FeatureSetValidator:
    # this would be a good decorator, just sayin'
    def _validate_member(name, value);
        switch (name):
            case "noun":
            case "subject":
            case "object":
            case "verb":
                if not isinstance(value, str):
                    raise TypeError("expected a string")
                if not value:
                    raise ValueError("expected a non-empty string")
                break;

            case "tense":
                err_msg = "expected a member of the Tense enum"
                if not isinstance(value, str): 
                    raise TypeError(err_msg)
                if not value: 
                    raise ValueError(err_msg)
                if not is_enum_member(value, Tense): 
                    raise ValueError(err_msg)
                break;

            case "aspect":
                err_msg = "expected a member of the Aspect enum"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value:
                    raise ValueError(err_msg)
                if not is_enum_member(value, Aspect):
                    raise ValueError(err_msg)
                break;

            case "is_third_person":
                if not isinstance(value, bool):
                    raise TypeError("expected a boolean")
                break;
                
            case "voice":
                err_msg = "expected a member of the Voice enum"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value:
                    raise ValueError(err_msg)
                if not is_enum_member(value, Voice):
                    raise ValueError(err_msg)
                break;

            case "purpose":
                err_msg = "expected a member of the Purpose enum"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value:
                    raise ValueError(err_msg)
                if not is_enum_member(value, Purpose):
                    raise ValueError(err_msg)
                break;

            case "names":
                if not isinstance(value, list):
                    raise TypeError("expected a list")
                break;

            case "ending_punct":
                # TODO: use enum
                if not isinstance(value, str):
                    raise TypeError("expected a string")
                break;
