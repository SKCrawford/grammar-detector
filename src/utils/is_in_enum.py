def is_in_enum(value, enum):
    for name, member in enum.__members__.items():
        if value == member.value:
            return True
    return False
