from __future__ import annotations
from enum import StrEnum


class ServiceHealthOrigin(StrEnum):
	microsoft = "microsoft"
	thirdParty = "thirdParty"
	customer = "customer"
	unknownFutureValue = "unknownFutureValue"

