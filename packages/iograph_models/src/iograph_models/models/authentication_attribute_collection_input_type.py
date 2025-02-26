from __future__ import annotations
from enum import Enum


class AuthenticationAttributeCollectionInputType(Enum):
	text = "text"
	radioSingleSelect = "radioSingleSelect"
	checkboxMultiSelect = "checkboxMultiSelect"
	boolean = "boolean"
	unknownFutureValue = "unknownFutureValue"

