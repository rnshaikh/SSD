from enum import Enum



class ProductType(Enum):

    CERTIFICATION = "CERTIFICATION"
    DEGREE = "DEGREE"
    DIPLOMA = "DIPLOMA"
    PRO_MEMBERSHIP = "PRO_MEMBERSHIP"
    ENROLLMENT = "ENROLLMENT"

    @classmethod
    def as_tuple(cls):
        return ((obj.value, obj.name.replace("_", " ")) for obj in cls)
