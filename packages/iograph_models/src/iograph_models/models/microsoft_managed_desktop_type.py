from __future__ import annotations
from enum import StrEnum


class MicrosoftManagedDesktopType(StrEnum):
	notManaged = "notManaged"
	premiumManaged = "premiumManaged"
	standardManaged = "standardManaged"
	starterManaged = "starterManaged"
	unknownFutureValue = "unknownFutureValue"

