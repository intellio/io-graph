from __future__ import annotations
from enum import Enum


class IdentityUserFlowAttributeInputType(Enum):
	textBox = "textBox"
	dateTimeDropdown = "dateTimeDropdown"
	radioSingleSelect = "radioSingleSelect"
	dropdownSingleSelect = "dropdownSingleSelect"
	emailBox = "emailBox"
	checkboxMultiSelect = "checkboxMultiSelect"

