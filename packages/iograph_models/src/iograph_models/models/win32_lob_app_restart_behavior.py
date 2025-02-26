from __future__ import annotations
from enum import Enum


class Win32LobAppRestartBehavior(Enum):
	basedOnReturnCode = "basedOnReturnCode"
	allow = "allow"
	suppress = "suppress"
	force = "force"

