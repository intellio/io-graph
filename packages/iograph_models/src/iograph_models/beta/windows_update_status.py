from __future__ import annotations
from enum import StrEnum


class WindowsUpdateStatus(StrEnum):
	upToDate = "upToDate"
	pendingInstallation = "pendingInstallation"
	pendingReboot = "pendingReboot"
	failed = "failed"

