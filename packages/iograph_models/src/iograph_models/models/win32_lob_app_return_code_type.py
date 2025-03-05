from __future__ import annotations
from enum import StrEnum


class Win32LobAppReturnCodeType(StrEnum):
	failed = "failed"
	success = "success"
	softReboot = "softReboot"
	hardReboot = "hardReboot"
	retry = "retry"

