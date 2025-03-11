from __future__ import annotations
from enum import StrEnum


class WindowsUpdateType(StrEnum):
	userDefined = "userDefined"
	all = "all"
	businessReadyOnly = "businessReadyOnly"
	windowsInsiderBuildFast = "windowsInsiderBuildFast"
	windowsInsiderBuildSlow = "windowsInsiderBuildSlow"
	windowsInsiderBuildRelease = "windowsInsiderBuildRelease"

