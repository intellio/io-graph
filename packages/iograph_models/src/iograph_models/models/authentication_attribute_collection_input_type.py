from __future__ import annotations
from enum import StrEnum


class AuthenticationAttributeCollectionInputType(StrEnum):
	text = "text"
	radioSingleSelect = "radioSingleSelect"
	checkboxMultiSelect = "checkboxMultiSelect"
	boolean = "boolean"
	unknownFutureValue = "unknownFutureValue"

