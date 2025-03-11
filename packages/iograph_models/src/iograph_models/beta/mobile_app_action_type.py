from __future__ import annotations
from enum import StrEnum


class MobileAppActionType(StrEnum):
	unknown = "unknown"
	installCommandSent = "installCommandSent"
	installed = "installed"
	uninstalled = "uninstalled"
	userRequestedInstall = "userRequestedInstall"

