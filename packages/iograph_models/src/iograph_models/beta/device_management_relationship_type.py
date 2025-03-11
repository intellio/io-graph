from __future__ import annotations
from enum import StrEnum


class DeviceManagementRelationshipType(StrEnum):
	and_ = "and_"
	or_ = "or_"
	unknownFutureValue = "unknownFutureValue"

