from __future__ import annotations
from enum import StrEnum


class DmaGuardDeviceEnumerationPolicyType(StrEnum):
	deviceDefault = "deviceDefault"
	blockAll = "blockAll"
	allowAll = "allowAll"

