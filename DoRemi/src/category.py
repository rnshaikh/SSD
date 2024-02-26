from enum import Enum

class StreamingCategory(Enum):
    MUSIC = "MUSIC"
    VIDEO = "VIDEO"
    PODCAST = "PODCAST"

    @classmethod
    def as_tuple(cls):
        return ((item.value, item.name) for item in cls)

    @classmethod
    def as_list(cls):
        return [item.value for item in cls]


class TopupCategory(Enum):

    FOUR_DEVICE = "FOUR_DEVICE"
    TEN_DEVICE = "TEN_DEVICE"

    @classmethod
    def as_tuple(cls):
        return ((item.value, item.name) for item in cls)

    @classmethod
    def as_list(cls):
        return [item.value for item in cls]


class PlanCategory(Enum):
    FREE = "FREE"
    PERSONAL = "PERSONAL"
    PREMIUM = "PREMIUM"

    @classmethod
    def as_tuple(cls):
        return ((item.value, item.name) for item in cls)

    @classmethod
    def as_list(cls):
        return [item.value for item in cls]
