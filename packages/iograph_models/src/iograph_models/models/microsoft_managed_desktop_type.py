from __future__ import annotations
from enum import Enum


class MicrosoftManagedDesktopType(Enum):
	notManaged = "notManaged"
	premiumManaged = "premiumManaged"
	standardManaged = "standardManaged"
	starterManaged = "starterManaged"
	unknownFutureValue = "unknownFutureValue"

