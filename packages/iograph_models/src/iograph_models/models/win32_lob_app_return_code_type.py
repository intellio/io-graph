from __future__ import annotations
from enum import Enum


class Win32LobAppReturnCodeType(Enum):
	failed = "failed"
	success = "success"
	softReboot = "softReboot"
	hardReboot = "hardReboot"
	retry = "retry"

