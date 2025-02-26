from __future__ import annotations
from enum import Enum


class TemplateApplicationLevel(Enum):
	none = "none"
	newPartners = "newPartners"
	existingPartners = "existingPartners"
	unknownFutureValue = "unknownFutureValue"

