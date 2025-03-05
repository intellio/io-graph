from __future__ import annotations
from enum import StrEnum


class AttributeType(StrEnum):
	String = "String"
	Integer = "Integer"
	Reference = "Reference"
	Binary = "Binary"
	Boolean = "Boolean"
	DateTime = "DateTime"

