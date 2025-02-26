from __future__ import annotations
from enum import Enum


class InstallState(Enum):
	notApplicable = "notApplicable"
	installed = "installed"
	failed = "failed"
	notInstalled = "notInstalled"
	uninstallFailed = "uninstallFailed"
	unknown = "unknown"

