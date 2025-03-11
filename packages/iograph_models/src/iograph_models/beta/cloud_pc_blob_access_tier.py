from __future__ import annotations
from enum import StrEnum


class CloudPcBlobAccessTier(StrEnum):
	hot = "hot"
	cool = "cool"
	cold = "cold"
	archive = "archive"
	unknownFutureValue = "unknownFutureValue"

