def is_enum_member(value, enum):
    for name, member in enum.__members__.items():
        if value == member.value:
            return True
    return False
