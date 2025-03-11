from __future__ import annotations
from enum import StrEnum


class AppsUpdateChannelType(StrEnum):
	current = "current"
	monthlyEnterprise = "monthlyEnterprise"
	semiAnnual = "semiAnnual"
	unknownFutureValue = "unknownFutureValue"

