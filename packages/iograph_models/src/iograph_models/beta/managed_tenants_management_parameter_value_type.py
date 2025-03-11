from __future__ import annotations
from enum import StrEnum


class ManagedTenantsManagementParameterValueType(StrEnum):
	string = "string"
	integer = "integer"
	boolean = "boolean"
	guid = "guid"
	stringCollection = "stringCollection"
	integerCollection = "integerCollection"
	booleanCollection = "booleanCollection"
	guidCollection = "guidCollection"
	unknownFutureValue = "unknownFutureValue"

