from __future__ import annotations
from enum import Enum


class AppsUpdateChannelType(Enum):
	current = "current"
	monthlyEnterprise = "monthlyEnterprise"
	semiAnnual = "semiAnnual"
	unknownFutureValue = "unknownFutureValue"

