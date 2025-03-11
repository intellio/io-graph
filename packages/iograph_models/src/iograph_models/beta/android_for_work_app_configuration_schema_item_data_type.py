from __future__ import annotations
from enum import StrEnum


class AndroidForWorkAppConfigurationSchemaItemDataType(StrEnum):
	bool = "bool"
	integer = "integer"
	string = "string"
	choice = "choice"
	multiselect = "multiselect"
	bundle = "bundle"
	bundleArray = "bundleArray"
	hidden = "hidden"

