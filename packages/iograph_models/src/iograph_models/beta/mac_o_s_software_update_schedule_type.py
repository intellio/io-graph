from __future__ import annotations
from enum import StrEnum


class MacOSSoftwareUpdateScheduleType(StrEnum):
	alwaysUpdate = "alwaysUpdate"
	updateDuringTimeWindows = "updateDuringTimeWindows"
	updateOutsideOfTimeWindows = "updateOutsideOfTimeWindows"

