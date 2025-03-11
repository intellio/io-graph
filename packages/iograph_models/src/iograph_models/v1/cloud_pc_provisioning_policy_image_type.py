from __future__ import annotations
from enum import StrEnum


class CloudPcProvisioningPolicyImageType(StrEnum):
	gallery = "gallery"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

