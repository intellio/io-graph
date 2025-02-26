from __future__ import annotations
from enum import Enum


class WindowsUpdateType(Enum):
	userDefined = "userDefined"
	all = "all"
	businessReadyOnly = "businessReadyOnly"
	windowsInsiderBuildFast = "windowsInsiderBuildFast"
	windowsInsiderBuildSlow = "windowsInsiderBuildSlow"
	windowsInsiderBuildRelease = "windowsInsiderBuildRelease"

