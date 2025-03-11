from __future__ import annotations
from enum import StrEnum


class Win32LobAppNotification(StrEnum):
	showAll = "showAll"
	showReboot = "showReboot"
	hideAll = "hideAll"

