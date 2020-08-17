from switch import Switch
from src.enum.Aspect import Aspect
from src.enum.Purpose import Purpose
from src.enum.Tense import Tense
from src.enum.Voice import Voice  
from src.util.is_in_enum import is_in_enum


class FeatureSetValidator:
    # this would be a good decorator, just sayin'
    def validate(self, name, value):
        print(f"Validating {name}: {value} (type {type(value)})")

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

            if case("person"):
                err_msg = "expected a Person enum member"
                if not isinstance(value, str):
                    raise TypeError(err_msg)
                if not value or not is_in_enum(value, Person):
                    raise ValueError(err_msg)

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
