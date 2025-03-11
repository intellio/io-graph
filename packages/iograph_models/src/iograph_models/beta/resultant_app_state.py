from __future__ import annotations
from enum import StrEnum


class ResultantAppState(StrEnum):
	notApplicable = "notApplicable"
	installed = "installed"
	failed = "failed"
	notInstalled = "notInstalled"
	uninstallFailed = "uninstallFailed"
	pendingInstall = "pendingInstall"
	unknown = "unknown"

