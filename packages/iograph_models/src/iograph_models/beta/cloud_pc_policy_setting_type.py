from __future__ import annotations
from enum import StrEnum


class CloudPcPolicySettingType(StrEnum):
	region = "region"
	singleSignOn = "singleSignOn"
	unknownFutureValue = "unknownFutureValue"

