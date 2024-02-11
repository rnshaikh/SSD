from enum import Enum


class PersonType(Enum):
	ADULT = "ADULT"
	SENIOR_CITIZEN = "SENIOR_CITIZEN"
	KID = "KID"

	@classmethod
	def as_tuple(cls):
		return ((item.value, item.name.replace("_", " ")) for item in cls)