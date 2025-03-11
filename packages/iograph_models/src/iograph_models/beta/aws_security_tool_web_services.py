from __future__ import annotations
from enum import StrEnum


class AwsSecurityToolWebServices(StrEnum):
	macie = "macie"
	wafShield = "wafShield"
	cloudTrail = "cloudTrail"
	inspector = "inspector"
	securityHub = "securityHub"
	detective = "detective"
	guardDuty = "guardDuty"
	unknownFutureValue = "unknownFutureValue"

