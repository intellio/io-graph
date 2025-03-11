from __future__ import annotations
from enum import StrEnum


class InstallState(StrEnum):
	notApplicable = "notApplicable"
	installed = "installed"
	failed = "failed"
	notInstalled = "notInstalled"
	uninstallFailed = "uninstallFailed"
	unknown = "unknown"

