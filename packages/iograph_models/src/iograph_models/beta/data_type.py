from __future__ import annotations
from enum import StrEnum


class DataType(StrEnum):
	none = "none"
	boolean = "boolean"
	int64 = "int64"
	double = "double"
	string = "string"
	dateTime = "dateTime"
	version = "version"
	base64 = "base64"
	xml = "xml"
	booleanArray = "booleanArray"
	int64Array = "int64Array"
	doubleArray = "doubleArray"
	stringArray = "stringArray"
	dateTimeArray = "dateTimeArray"
	versionArray = "versionArray"

