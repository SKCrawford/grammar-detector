from src.enums.Feature import Feature
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
            raise Exception("call spawn() before set() or build()")
        if not hasattr(self._instance, field):
            raise ValueError("invalid field name")

        if self._validator:
            self._validator.validate(field, val)

        setattr(self._instance, field, val)
        return self

    def build(self):
        if not self._instance:
            raise Exception("call spawn() before set() or build()")
        return self._instance
