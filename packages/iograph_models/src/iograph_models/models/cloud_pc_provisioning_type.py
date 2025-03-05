from __future__ import annotations
from enum import StrEnum


class CloudPcProvisioningType(StrEnum):
	dedicated = "dedicated"
	shared = "shared"
	unknownFutureValue = "unknownFutureValue"

