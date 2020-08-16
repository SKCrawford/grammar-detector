from src.enums.Feature import Feature
from src.utils.is_enum_member import is_enum_member
from .FeatureSet import FeatureSet


class Builder:
    _product_klass = None
    _instance = None
    _validator = None
    _validator_klass = None

    def __init__(self, product_klass, validator_klass=None):
        self._product_klass = product_klass
        self._validator_klass = validator_klass

    def spawn(self):
        self._instance = self._product_klass()
        if self._validator_klass:
            self._validator = self._validator_klass()
        return self

    def set(self, field, val):
        if not self._instance:
            raise Exception("call spawn() before setting")
        if not hasattr(self._instance, field):
            raise ValueError("invalid field name")

        if self._validator:
            self._validator.validate(field, val)

        setattr(self._instance, field, val)
        return self

    def build(self):
        return self._instance
