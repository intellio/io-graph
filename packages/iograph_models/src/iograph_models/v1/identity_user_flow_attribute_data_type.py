from __future__ import annotations
from enum import StrEnum


class IdentityUserFlowAttributeDataType(StrEnum):
	string = "string"
	boolean = "boolean"
	int64 = "int64"
	stringCollection = "stringCollection"
	dateTime = "dateTime"
	unknownFutureValue = "unknownFutureValue"

