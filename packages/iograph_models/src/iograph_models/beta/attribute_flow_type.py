from __future__ import annotations
from enum import StrEnum


class AttributeFlowType(StrEnum):
	Always = "Always"
	ObjectAddOnly = "ObjectAddOnly"
	MultiValueAddOnly = "MultiValueAddOnly"
	ValueAddOnly = "ValueAddOnly"
	AttributeAddOnly = "AttributeAddOnly"

