from __future__ import annotations
from enum import StrEnum


class Win32LobAppRestartBehavior(StrEnum):
	basedOnReturnCode = "basedOnReturnCode"
	allow = "allow"
	suppress = "suppress"
	force = "force"

