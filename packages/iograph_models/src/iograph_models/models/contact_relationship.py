from __future__ import annotations
from enum import StrEnum


class ContactRelationship(StrEnum):
	parent = "parent"
	relative = "relative"
	aide = "aide"
	doctor = "doctor"
	guardian = "guardian"
	child = "child"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

