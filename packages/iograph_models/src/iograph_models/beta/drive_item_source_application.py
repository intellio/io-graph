from __future__ import annotations
from enum import StrEnum


class DriveItemSourceApplication(StrEnum):
	teams = "teams"
	yammer = "yammer"
	sharePoint = "sharePoint"
	oneDrive = "oneDrive"
	stream = "stream"
	powerPoint = "powerPoint"
	office = "office"
	loki = "loki"
	loop = "loop"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

