from __future__ import annotations
from enum import Enum


class CloudPcProvisioningType(Enum):
	dedicated = "dedicated"
	shared = "shared"
	unknownFutureValue = "unknownFutureValue"

