from __future__ import annotations
from enum import Enum


class DriveItemSourceApplication(Enum):
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

