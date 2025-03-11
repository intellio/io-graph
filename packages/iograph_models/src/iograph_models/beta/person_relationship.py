from __future__ import annotations
from enum import StrEnum


class PersonRelationship(StrEnum):
	manager = "manager"
	colleague = "colleague"
	directReport = "directReport"
	dotLineReport = "dotLineReport"
	assistant = "assistant"
	dotLineManager = "dotLineManager"
	alternateContact = "alternateContact"
	friend = "friend"
	spouse = "spouse"
	sibling = "sibling"
	child = "child"
	parent = "parent"
	sponsor = "sponsor"
	emergencyContact = "emergencyContact"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

