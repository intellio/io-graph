from __future__ import annotations
from enum import StrEnum


class CloudPcStorageAccountAccessTier(StrEnum):
	hot = "hot"
	cool = "cool"
	premium = "premium"
	cold = "cold"
	unknownFutureValue = "unknownFutureValue"

