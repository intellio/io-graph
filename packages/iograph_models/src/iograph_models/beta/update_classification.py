from __future__ import annotations
from enum import StrEnum


class UpdateClassification(StrEnum):
	userDefined = "userDefined"
	recommendedAndImportant = "recommendedAndImportant"
	important = "important"
	none = "none"

