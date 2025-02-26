from __future__ import annotations
from enum import Enum


class ContactRelationship(Enum):
	parent = "parent"
	relative = "relative"
	aide = "aide"
	doctor = "doctor"
	guardian = "guardian"
	child = "child"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

