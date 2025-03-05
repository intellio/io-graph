from __future__ import annotations
from enum import StrEnum


class IdentityUserFlowAttributeInputType(StrEnum):
	textBox = "textBox"
	dateTimeDropdown = "dateTimeDropdown"
	radioSingleSelect = "radioSingleSelect"
	dropdownSingleSelect = "dropdownSingleSelect"
	emailBox = "emailBox"
	checkboxMultiSelect = "checkboxMultiSelect"

