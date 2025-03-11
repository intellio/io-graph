from __future__ import annotations
from enum import StrEnum


class DirectoryDefinitionDiscoverabilities(StrEnum):
	None_ = "None_"
	AttributeNames = "AttributeNames"
	AttributeDataTypes = "AttributeDataTypes"
	AttributeReadOnly = "AttributeReadOnly"
	ReferenceAttributes = "ReferenceAttributes"
	UnknownFutureValue = "UnknownFutureValue"

