from __future__ import annotations
from enum import StrEnum


class CloudLicensingAssigneeTypes(StrEnum):
	none = "none"
	user = "user"
	group = "group"
	device = "device"
	unknownFutureValue = "unknownFutureValue"

