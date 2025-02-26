from __future__ import annotations
from enum import Enum


class ServiceHealthOrigin(Enum):
	microsoft = "microsoft"
	thirdParty = "thirdParty"
	customer = "customer"
	unknownFutureValue = "unknownFutureValue"

