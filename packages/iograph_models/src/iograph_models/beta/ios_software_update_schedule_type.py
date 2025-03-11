from __future__ import annotations
from enum import StrEnum


class IosSoftwareUpdateScheduleType(StrEnum):
	updateOutsideOfActiveHours = "updateOutsideOfActiveHours"
	alwaysUpdate = "alwaysUpdate"
	updateDuringTimeWindows = "updateDuringTimeWindows"
	updateOutsideOfTimeWindows = "updateOutsideOfTimeWindows"

