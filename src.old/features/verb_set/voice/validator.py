from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum import Voice
from .model import VoiceFeature


@is_type(VoiceFeature)
@is_truthy
def validate_voice_feature(feature):
    _validate_voice(feature.value)


@is_type(str)
@is_truthy
@is_in_enum(Voice)
def _validate_voice(voice):
    pass
