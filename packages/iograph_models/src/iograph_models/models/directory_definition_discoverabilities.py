from __future__ import annotations
from enum import Enum


class DirectoryDefinitionDiscoverabilities(Enum):
	None_ = "None_"
	AttributeNames = "AttributeNames"
	AttributeDataTypes = "AttributeDataTypes"
	AttributeReadOnly = "AttributeReadOnly"
	ReferenceAttributes = "ReferenceAttributes"
	UnknownFutureValue = "UnknownFutureValue"

