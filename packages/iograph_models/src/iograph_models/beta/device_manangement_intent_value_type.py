from __future__ import annotations
from enum import StrEnum


class DeviceManangementIntentValueType(StrEnum):
	integer = "integer"
	boolean = "boolean"
	string = "string"
	complex = "complex"
	collection = "collection"
	abstractComplex = "abstractComplex"

