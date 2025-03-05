from __future__ import annotations
from enum import StrEnum


class TemplateApplicationLevel(StrEnum):
	none = "none"
	newPartners = "newPartners"
	existingPartners = "existingPartners"
	unknownFutureValue = "unknownFutureValue"

