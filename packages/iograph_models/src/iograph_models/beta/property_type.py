from __future__ import annotations
from enum import StrEnum


class PropertyType(StrEnum):
	string = "string"
	int64 = "int64"
	double = "double"
	dateTime = "dateTime"
	boolean = "boolean"
	stringCollection = "stringCollection"
	int64Collection = "int64Collection"
	doubleCollection = "doubleCollection"
	dateTimeCollection = "dateTimeCollection"

