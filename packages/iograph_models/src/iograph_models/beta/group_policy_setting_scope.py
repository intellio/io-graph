from __future__ import annotations
from enum import StrEnum


class GroupPolicySettingScope(StrEnum):
	unknown = "unknown"
	device = "device"
	user = "user"

