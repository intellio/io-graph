from __future__ import annotations
from enum import Enum


class CloudPcProvisioningPolicyImageType(Enum):
	gallery = "gallery"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

