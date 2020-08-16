from switch import Switch
from src.enums.Tense import Tense
from src.enums.Aspect import Aspect
from src.enums.Voice import Voice  
from src.enums.Purpose import Purpose
from src.utils.is_in_enum import is_in_enum


class FeatureSetValidator:
    # this would be a good decorator, just sayin'
    def validate(self, name, value):
        print(f"Validating {name}: {value}")

        with Switch(name) as case:
            if case("noun", "subject", "object", "verb"):
                err_msg = "expected a non-empty string"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value:
                    raise ValueError(err_msg)

            if case("tense"):
                err_msg = "expected a Tense enum member"
                if not isinstance(value, str): 
                    raise TypeError(err_msg)
                if not value or not is_in_enum(value, Tense):
                    raise ValueError(err_msg)

            if case("aspect"):
                err_msg = "expected a Aspect enum member"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value or not is_in_enum(value, Aspect):
                    raise ValueError(err_msg)

            if case("is_third_person"):
                if not value is None and not isinstance(value, bool):
                    raise TypeError("expected a boolean or None")

            if case("voice"):
                err_msg = "expected a Voice enum member"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value or not is_in_enum(value, Voice):
                    raise ValueError(err_msg)

            if case("purpose"):
                err_msg = "expected a Purpose enum member"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value or not is_in_enum(value, Purpose):
                    raise ValueError(err_msg)

            if case("names"):
                if not isinstance(value, list):
                    raise TypeError("expected a list")

            if case("ending_punct"):
                if not isinstance(value, str):
                    raise TypeError("expected a string")
