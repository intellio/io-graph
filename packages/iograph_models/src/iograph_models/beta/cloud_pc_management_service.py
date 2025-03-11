from __future__ import annotations
from enum import StrEnum


class CloudPcManagementService(StrEnum):
	windows365 = "windows365"
	devBox = "devBox"
	unknownFutureValue = "unknownFutureValue"
	rpaBox = "rpaBox"

