from __future__ import annotations
from enum import StrEnum


class MobileAppDependencyType(StrEnum):
	detect = "detect"
	autoInstall = "autoInstall"
	unknownFutureValue = "unknownFutureValue"

