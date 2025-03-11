from __future__ import annotations
from enum import StrEnum


class WinGetAppNotification(StrEnum):
	showAll = "showAll"
	showReboot = "showReboot"
	hideAll = "hideAll"
	unknownFutureValue = "unknownFutureValue"

